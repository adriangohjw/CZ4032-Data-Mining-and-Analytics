from pprint import pprint
import pandas as pd


class RuleSelection:

  def __init__(self, data, classifiers):
    self.data = data
    self.classifiers = classifiers


  def call(self, attribute):
    self.data['guess'] = None
    classifier_indexes_to_drop = []

    for rule in self.classifiers:
      print(">>>>> Guessing for rule...")
      print(rule)

      selected_rows = self.generate_matching_rows(rule)
      selected_row_indexes = selected_rows.index.values.tolist()
      if len(selected_row_indexes) > 0:
        self.guess_rows_with_value(selected_row_indexes, rule['consequents'])
      else:
        print("Discarding rule because no matching rows found")
        classifier_indexes_to_drop.append(rule['index'])

      print()
  
    self.remove_classifiers_with_no_matching_rows(classifier_indexes_to_drop)
    self.mark_unclassified_data_with_default_class(attribute)


  def generate_matching_rows(self, rule):
    selected_rows = self.data[
      self.data['guess'].isnull()
    ]

    for key, value in rule['antecedents'].items():
      selected_rows = selected_rows[
        selected_rows[key].str.split().apply(lambda x: len(set(x).intersection(set(value)))) > 0
      ]

    return selected_rows


  def guess_rows_with_value(self, indexes, value):
    self.data.loc[
      self.data.index.isin(indexes),
      'guess'
    ] = value


  def remove_classifiers_with_no_matching_rows(self, indexes):
    self.classifiers[:] = [x for x in self.classifiers if not x['index'] in indexes]


  def mark_unclassified_data_with_default_class(self, colname_of_attribute):
    unclassified_data = self.data[
      self.data['guess'].isnull()
    ]

    if self.most_occured_value_in_col(unclassified_data, colname_of_attribute) is None:
      return
    
    self.data.loc[
      unclassified_data.index,
      'guess'
    ] = self.most_occured_value_in_col(unclassified_data, colname_of_attribute)


  def most_occured_value_in_col(self, data, colname):
    values = data[colname].value_counts()[:1].index.tolist()
    if values == []:
      return None
    else:
      return values[0]
