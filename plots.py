import plotly.express as px
from dfplots import df_receitaEstado, df_receitaContagemVendasVendedor
from dfplots import df_receitaMensal, df_receitaCategoria

#plotar grafico de mapa (receita por estado)
plotMapEstado = px.scatter_geo(
    data_frame= df_receitaEstado,
    lat='lat',
    lon='lon',
    scope='south america',
    size='Preço',
    template='seaborn',
    hover_name='Local da compra',
    hover_data={'lat':False, 'lon':False},
    title='Receita por Estado')

#plotar o gráfico da receita por mês
plotLinePrecoMensal = px.line(
    data_frame = df_receitaMensal,
    x = 'Mes',
    y = 'Preço',
    markers= True,
    range_y=(0,df_receitaMensal.max()),
    color = 'Ano',
    title='Receita Mensal'
)    
plotLinePrecoMensal.update_layout(yaxis_title='Receita')

#plotar o gráfico da receita por estado
#vamos usar o mesmo dataframe df_receitaEstado
plotReceitaEstado = px.bar(
    data_frame=df_receitaEstado.head(7),
    x = 'Local da compra',
    y = 'Preço',
    text_auto=True, 
    title='Top 7 receita por estados'
)

#plotar o gráfico da receita por categoria (7 melhores)
plotReceitaCategoria = px.bar(
    data_frame=df_receitaCategoria.head(7),
    text_auto=True,
    title='Top 7 categorias com maior receita',
)

#plotar o gráfico da receita por vendedor
plotReceitaVendedor = px.bar (
    df_receitaContagemVendasVendedor[['sum']].sort_values('sum', ascending=False).head(7),
    x = 'sum',
    y = df_receitaContagemVendasVendedor[['sum']].sort_values('sum', ascending=False).head(7).index,
    text_auto=True,
    title = 'Top 7 vendedores por receita',
    width=450
)

#plotar o gráfico da quantidade de vendas por vendedor
plotVendasVendedor = px.bar (
    df_receitaContagemVendasVendedor[['count']].sort_values('count', ascending=False).head(7),
    x = 'count',
    y = df_receitaContagemVendasVendedor[['count']].sort_values('count', ascending=False).head(7).index,
    text_auto=True,
    title = 'Top 7 vendedores por qtd de vendas',
    width=450
)