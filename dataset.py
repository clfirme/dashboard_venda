import json
import pandas as pd

#coleta e leitura de dados json
fl = open('./vendas.json')
data = json.load(fl)

#print(data)

# arquivos json tem estrutura em dicionario (dict)
df = pd.DataFrame.from_dict(data) # pedimos ao pandas para transformar estrutura de dicionario em dataframe
#print(df)
#print(df['Data da Compra'])#observamos que a categoria 'Data da Compra' estah em formato de objeto dtype: object
df['Data da Compra']=pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y') #Vamos passar a categoria 'Data da Compra' para datetime
#print(df['Data da Compra']) #agora vemos 'Data da Compra' em dtype: datetime64[ns]
pd.set_option('display.max_columns', None)
#print(df.head())

fl.close()
