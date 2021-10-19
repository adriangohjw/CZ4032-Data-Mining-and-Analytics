from pprint import pprint
from data_processor import load_dataset, clean_dataframe, get_binning_references, bin_dataframe, filter_df_columns, append_col_name_to_dataframe, get_frequent_itemsets, get_association_rules, unmap_classifiers_with_binning_refereces, graphing
from classifier_generator import ClassifierGenerator
from rule_selection import RuleSelection
from accuracy_analyzer import AccuracyAnalyzer
from performance_analyzer import get_df_memory_size
import time

import numpy

DATA_SOURCE = 'data/adult_cleaned.csv'
DELIMITER = ','
attributes = [

  'workclass', 'education', 'marital-status', 'occupation',
  'relationship', 'race', 'sex', 'native-country', 'income-group'
]
attribute_to_classify = 'income-group'

data = load_dataset(DATA_SOURCE, DELIMITER)
data_with_selected_attributes = filter_df_columns(data, attributes)

binning_references = get_binning_references(data_with_selected_attributes)
bin_dataframe(data_with_selected_attributes, binning_references)

df_with_appended_column_names = append_col_name_to_dataframe(data_with_selected_attributes)

print(get_df_memory_size(df_with_appended_column_names))

start = time.process_time()

#testing the change for qn5, try different support levels
#Assign 0 to accuracy if too many rules in rulebase
min_sup = []
accuracy_graph = []
for i in range(1,20):
    j = i/20
    min_sup.append(j)
    
    try:
        frequent_items = get_frequent_itemsets(df_with_appended_column_names, min_support=j)
        assoc_rules = get_association_rules(frequent_items)

        cg = ClassifierGenerator(assoc_rules, attribute_to_classify)
        classifiers = cg.classifiers

        test_data = data.copy()
        binning_references = get_binning_references(test_data)
        bin_dataframe(test_data, binning_references)

        rs = RuleSelection(test_data, classifiers)
        rs.call(attribute_to_classify)

        classifiers = rs.classifiers
        unmap_classifiers_with_binning_refereces(classifiers, binning_references)
        pprint(classifiers)
        print()

        aa = AccuracyAnalyzer(rs.data)
        accuracy = aa.call(attribute_to_classify)
        accuracy_graph.append(accuracy)
    except:
        accuracy_graph.append(0.0)

graphing(min_sup,accuracy_graph)
