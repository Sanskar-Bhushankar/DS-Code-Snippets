def data_info(data):
  data_dict=pd.DataFrame(columns=["column","count","unique_values","Range","Null Values","Possible Values"])
  for col in data.columns:
    count=data[col].shape[0]
    unique_values=data[col].nunique()
    if unique_values>1:
      range=f"{data[col].min()}-{data[col].max()}"
    else:
      range=np.nan
    null_values=data[col].isnull().sum()
    possible_values=list(data[col].sample(frac=0.25,replace=False,random_state=42).unique())
    if len(possible_values)>10:
      possible_values=possible_values[:6]
    data_dict.loc[len(data_dict.index)]=[col,count,unique_values,range,null_values,possible_values]
  return data_dict

