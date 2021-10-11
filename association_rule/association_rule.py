from data_processor import load_dataset, get_frequent_itemsets, get_association_rules

DATA_SOURCE = 'data/adult_cleaned.csv'
DELIMITER = ','
attributes = [
  'workclass', 'education', 'marital-status', 'occupation',
  'relationship', 'race', 'sex', 'native-country', 'income-group'
]

data = load_dataset(DATA_SOURCE, DELIMITER)
frequent_items = get_frequent_itemsets(data, min_support=0.5, colnames=attributes)
assoc_rules = get_association_rules(frequent_items)
print(assoc_rules)
