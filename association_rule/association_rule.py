from data_processor import load_dataset, filter_df_columns, append_col_name_to_dataframe, get_frequent_itemsets, get_association_rules

DATA_SOURCE = 'data/adult_cleaned.csv'
DELIMITER = ','
attributes = [
  'workclass', 'education', 'marital-status', 'occupation',
  'relationship', 'race', 'sex', 'native-country', 'income-group'
]

data = load_dataset(DATA_SOURCE, DELIMITER)
data_with_selected_attributes = filter_df_columns(data, attributes)
df_with_appended_column_names = append_col_name_to_dataframe(data_with_selected_attributes)
frequent_items = get_frequent_itemsets(df_with_appended_column_names, min_support=0.5)
assoc_rules = get_association_rules(frequent_items)
print(assoc_rules)
