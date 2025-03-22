def preprocessCSV(csv_file, output_dataframe, regex):
  
  df = pd.read_csv('csv_file') # read csv file
  
  df_filt = df.filter(regex=(".*14dhist|.*7dhist")) # filter column
  df_filt.dropna(inplace=True)
  
  df_str = df_filt.select_dtypes(object) # select only object columns, copy to new dataframe

for col in df_W1_BT_mxscale_str.columns:
    df_W1_BT_mxscale_str[col] = df_W1_BT_mxscale_str[col].replace({'l': 0.0, 'm': 0.5, 'h': 1.0}) # low, medium, high normalised to 0, 0.5, 1

df_W1_BT_mxscale_str = df_W1_BT_mxscale_str.astype(float) # convert to float


df_W1_BT_mxscale = df_W1_BT_filt.select_dtypes(include=['float64']) # select only float columns

for col in df_W1_BT_mxscale.columns:
    df_W1_BT_mxscale[col] = df_W1_BT_mxscale[col] / df_W1_BT_mxscale[col].abs().max() # min max scaling

df_W1_BT = pd.concat([df_W1_BT_mxscale, df_W1_BT_mxscale_str], axis=1).reindex(df_W1_BT_mxscale.index) # combine the two dataframes
del df_W1_BT_mxscale, df_W1_BT_mxscale_str # delete the temporary dataframes
