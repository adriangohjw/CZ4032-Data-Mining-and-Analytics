import pandas as pd

def get_df_memory_size(df):
  memory_in_byte = df.memory_usage(deep=True).sum()
  memory_in_mb = df.memory_usage(deep=True).sum() / 1000000
  return ">>>>> Memory used for this dataframe is: " + str(round(memory_in_mb)) + "MB"
