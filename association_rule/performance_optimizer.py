def get_optimized_df_and_dict(df):
  reference_dict = {}
  
  index = 0
  for col in list(df):
    for value in df[col].unique():
      reference_dict[index] = value
      df[col].replace({value: index}, inplace=True)
      index += 1

  return df, reference_dict

def repopulate_assoc_rules(assoc_rules, reference_dict):
  repopulate_cols('antecedents', assoc_rules, reference_dict)
  repopulate_cols('consequents', assoc_rules, reference_dict)

def repopulate_cols(colname, assoc_rules, reference_dict):
  for group in assoc_rules[colname]:
    original_values = []
    for item in list(group):
      original_value = reference_dict.get(item)
      if original_value is None:
        original_values.append(item)
      else:
        original_values.append(original_value)
      
      assoc_rules[colname].replace({group: frozenset(original_values)}, inplace=True)
