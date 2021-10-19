import pandas as pd
import numpy as np
import math
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules


def delimiter():
  return '___'


def load_dataset(filename, delimiter):
  return pd.read_csv(filename, index_col=False, delimiter=delimiter)


def clean_dataframe(df):
  return df.dropna()


def get_full_dataframe(dataframe, count_col_name):
  lowest_count = dataframe[count_col_name].min()
  expanded_data_list = []

  for _, row in dataframe.iterrows():
    count = row[count_col_name]
    normalised_count = round(count / lowest_count)
    for _ in range(normalised_count):
      expanded_data_list.append(row)

  return pd.DataFrame(expanded_data_list)


def get_binning_references(df):
  binning_references = {}
  for column in df.columns: 
    if df[column].dtype in ['int64', 'float64']:
      binning_references[column] = get_bin_means(df[column].tolist())
  
  return binning_references


def get_bin_means(data):
  results = []

  a = np.array(data)
  for i in range(9):
    results.append(
      np.percentile(a, (i + 1) * 10)
    )

  return results


def bin_dataframe(df, binning_references):
  for colname, references in binning_references.items():
    mapping_references = {}

    min_value = 0
    for index, item in enumerate(references):
      mapping_references[index] = list(
        df[
          df[colname].between(min_value, item)
        ].index
      )
      min_value = item

    mapping_references[len(references)] = list(
        df[
          df[colname] >= min_value
        ].index
      )

    for i, indexes in mapping_references.items():
      df.loc[df.index.isin(indexes), colname] = colname + str(i)


def unmap_classifiers_with_binning_refereces(classifiers, binning_references):
  for classifier in classifiers:
    for colname, values in classifier['antecedents'].items():
      if colname not in binning_references.keys():
        continue

      classifier['antecedents'][colname] = rehydrate_values(
        values, colname, binning_references[colname]
      )


def rehydrate_values(values, colname, references):
  results = []

  for value in values:
    index = int(value[len(colname):])

    if index == 0:
      results.append("less than " + str(references[index]))
      continue

    if index == len(references):
      results.append("more than " + str(references[index-1]))
      continue
  
    results.append(
      str(references[index - 1]) + " to " + str(references[index])
    )

  return results


def df_to_lists_of_list(df):
  return df.values.tolist()


def encode_df(df):
  te = TransactionEncoder()
  te_ary = te.fit(df).transform(df)
  result = pd.DataFrame(te_ary, columns=te.columns_)

  return result


def filter_df_columns(df, colnames=None):
  filtered_df = df if colnames is None else df[colnames]
  return filtered_df


def append_col_name_to_dataframe(df):
  for col in list(df.columns):
    df[col] = col + delimiter() + df[col].astype(str)
  
  return df


def get_frequent_itemsets(df, min_support=0.6):
  df_lol = df_to_lists_of_list(df)
  encoded_data = encode_df(df_lol)
  freq_items = apriori(encoded_data, min_support=min_support, use_colnames=True)

  return freq_items


def get_association_rules(freq_items):
  rules = association_rules(freq_items, metric='lift', min_threshold=1)
  rules = rules.sort_values(['confidence', 'lift'], ascending =[False, False])

  return rules
