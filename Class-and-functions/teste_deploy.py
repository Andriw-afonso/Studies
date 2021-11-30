def teste_deploy(df,model,caminho_do_modelo,df_desejado):

  model=pickle.load(open(caminho_do_modelo,'rb'))

  t=transformations()
  df1=t.data_cleaning(df)  
  df2=t.feature_engeneering(df1)  
  df3=t.data_preparation(df2)  
  df4=t.get_prediction(model,df,df3)  

  if df_desejado=='df1':
    a=df1
  elif df_desejado=='df2':
    a=df2
  elif df_desejado=='df3':
    a=df3
  elif df_desejado=='df4':
    a=df4
  return a