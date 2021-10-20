import pandas as pd

def get_df_memory_size(df):
  memory_in_byte = df.memory_usage(deep=True).sum()
  memory_in_mb = float(df.memory_usage(deep=True).sum()) / float(1000000)
  return ">>>>> Memory used for this dataframe is: " + str(memory_in_mb) + "MB"
