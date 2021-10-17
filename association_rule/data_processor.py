import pandas as pd
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


def df_to_lists_of_list(df):
  return df.values.tolist()


def encode_df(df):
  te = TransactionEncoder()
  te_ary = te.fit(df).transform(df)
  result = pd.DataFrame(te_ary, columns=te.columns_)

  return result


def append_col_name_to_dataframe(df):
  for col in list(df.columns):
    df[col] = col + delimiter() + df[col]
  
  return df


def get_frequent_itemsets(df, min_support=0.6, colnames=None):
  filtered_df = df if colnames is None else df[colnames]
  filtered_df = append_col_name_to_dataframe(filtered_df)
  filtered_df_lol = df_to_lists_of_list(filtered_df)
  encoded_data = encode_df(filtered_df_lol)
  freq_items = apriori(encoded_data, min_support=min_support, use_colnames=True)

  return freq_items


def get_association_rules(freq_items):
  rules = association_rules(freq_items, metric='lift', min_threshold=1)
  rules = rules.sort_values(['confidence', 'lift'], ascending =[False, False])

  return rules
