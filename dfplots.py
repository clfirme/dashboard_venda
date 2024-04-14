from dataset import df
import pandas as pd

#aqui vamos criar um dataframe específico para construir cada gráfico 
#a partir do dataframe original (df)
#print(df)

#1-dataframe receita por estado (primeiro dataframe para fazer grafico)
df_receitaEstado = df.groupby('Local da compra')[['Preço']].sum().sort_values('Preço', ascending=False)
#drop_duplicates elimina registros duplicados e acrescenta as colunas 'lat' e 'lon' na tabela
df_receitaEstado=df.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']].merge(df_receitaEstado, left_on='Local da compra', right_index=True).sort_values('Preço', ascending=False)
#print(df_receitaEstado) 

#2-dataframe receita mensal (segundo dataframe para fazer grafico)
#set_index('Data da compra') - geralmente o id é o índice da tabela e será trocado por mês
#vamos agrupar o somatorio do preço por mês
#A Grouper allows the user to specify a groupby instruction for an object.
#freq  will groupby the specified frequency if the target selection (via key or level) is a datetime-like object. 
df_receitaMensal = df.set_index('Data da Compra').groupby(pd.Grouper(freq='ME'))['Preço'].sum().reset_index()
#print(df_receitaMensal)
#extrair a informação do ano e mês da categoria Data da Compra
df_receitaMensal['Ano']=df_receitaMensal['Data da Compra'].dt.year
df_receitaMensal['Mes']=df_receitaMensal['Data da Compra'].dt.month_name()
#print(df_receitaMensal)#a tabela aparece agora com as colunas Ano e Mes ao lado direito da coluna Preço

#3-dataframe de receitas por categoria(terceiro dataframe para fazer gráfico)
df_receitaCategoria = df.groupby('Categoria do Produto')[['Preço']].sum().sort_values('Preço', ascending=False)
#print(df_receitaCategoria.head())

#4-dataframe receita por vendedores e contagem de vendas
df_receitaContagemVendasVendedor=pd.DataFrame(df.groupby('Vendedor')['Preço'].agg(['sum','count']))
#print(df_receitaContagemVendasVendedor)