import pandas as pd
from data_processor import delimiter

class ClassifierGenerator:

  def __init__(self, assoc_rules, attribute_to_classify):
    self.assoc_rules = assoc_rules
    self.filtered_assoc_rules = self.filter_df_for_one_consequent_type(
      self.assoc_rules, attribute_to_classify
    )
    self.classifiers = self.generate_classifiers(
      self.filtered_assoc_rules
    )


  def filter_df_for_one_consequent_type(self, assoc_rules, attribute):
    assoc_rules_copy = assoc_rules.copy()
    for index, rule in assoc_rules_copy.iterrows():

      if len(rule['consequents']) > 1:
        assoc_rules_copy.drop(index, inplace=True)
        continue

      consequent_attr = list(rule['consequents'])[0].split(delimiter())[0]
      if consequent_attr != attribute:
        assoc_rules_copy.drop(index, inplace=True)
        continue

    return assoc_rules_copy


  def generate_classifiers(self, assoc_rules):
    classifiers = []

    index = 0
    for _, rule in assoc_rules.iterrows():
      classifiers.append(
        {
          "index": index,
          "antecedents": self.generate_antecedents_dict(list(rule['antecedents'])),
          "consequents": list(rule['consequents'])[0].split(delimiter())[1]
        }
      )
      index += 1

    return classifiers


  def generate_antecedents_dict(self, antecedents):
    result = {}

    for antecedent in antecedents:
      key, value = antecedent.split(delimiter())
      if key in result:
        result[key].append(value)
      else:
        result[key] = [value]

    return result


  def sorted_assoc_rules(self):
    return self.assoc_rules.sort_values(['confidence', 'support'], ascending=[False, False])
