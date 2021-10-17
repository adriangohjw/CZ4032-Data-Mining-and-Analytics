from pprint import pprint
from data_processor import load_dataset, get_frequent_itemsets, get_association_rules
from classifier_generator import ClassifierGenerator
from rule_selection import RuleSelection
from accuracy_analyzer import AccuracyAnalyzer

DATA_SOURCE = 'data/adult_cleaned.csv'
DELIMITER = ','
attributes = [
  'workclass', 'education', 'marital-status', 'occupation',
  'relationship', 'race', 'sex', 'native-country', 'income-group'
]
attribute_to_classify = 'income-group'

data = load_dataset(DATA_SOURCE, DELIMITER)
frequent_items = get_frequent_itemsets(data, min_support=0.5, colnames=attributes)
assoc_rules = get_association_rules(frequent_items)

cg = ClassifierGenerator(assoc_rules, attribute_to_classify)
classifiers = cg.classifiers

rs = RuleSelection(data, classifiers)
rs.call(attribute_to_classify)
pprint(rs.classifiers)

aa = AccuracyAnalyzer(rs.data)
accuracy = aa.call(attribute_to_classify)
print(accuracy)