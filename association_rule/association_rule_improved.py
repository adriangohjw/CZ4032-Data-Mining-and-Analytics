from pprint import pprint
from data_processor import load_dataset, filter_df_columns, append_col_name_to_dataframe, get_binning_references, bin_dataframe, get_frequent_itemsets, get_association_rules
from performance_analyzer import get_df_memory_size
from performance_optimizer import get_optimized_df_and_dict, repopulate_assoc_rules
import time
import sys

#input directory for the dataset to be analysed
DATA_SOURCE = 'data/adult_cleaned.csv'
DELIMITER = ','
#input all the attributes to be used for analysis
attributes = [
  'age', 'hours-per-week',
  'workclass', 'education', 'marital-status', 'occupation',
  'relationship', 'race', 'sex', 'native-country', 'income-group'
]

data = load_dataset(DATA_SOURCE, DELIMITER)
data_with_selected_attributes = filter_df_columns(data, attributes)

binning_references = get_binning_references(data_with_selected_attributes)
bin_dataframe(data_with_selected_attributes, binning_references)

df_with_appended_column_names = append_col_name_to_dataframe(data_with_selected_attributes)

start = time.process_time()
df_optimized, reference_dict = get_optimized_df_and_dict(df_with_appended_column_names)
elapsed_time = time.process_time() - start
print(">>>>> Time to determine optimize dataframe: " + str(elapsed_time) + "secs")
print(get_df_memory_size(df_optimized))
print(">>>>> The size of the dictionary is {} bytes".format(sys.getsizeof(reference_dict)))

start = time.process_time()
frequent_items = get_frequent_itemsets(df_with_appended_column_names, min_support=0.5)
assoc_rules = get_association_rules(frequent_items)
repopulate_assoc_rules(assoc_rules, reference_dict)
elapsed_time = time.process_time() - start
print(">>>>> Time to determine assoc rules: " + str(elapsed_time) + "secs")
