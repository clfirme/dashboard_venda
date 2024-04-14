import streamlit as st
import plotly.express as px
import pandas as pd
from dataset import df
from utils import format_number
from plots import plotMapEstado, plotLinePrecoMensal
from plots import plotReceitaEstado, plotReceitaCategoria
from plots import plotReceitaVendedor, plotVendasVendedor

st.set_page_config(layout='wide')
st.title("Dashboard de Vendas :shopping_trolley:")

#adição de filtro por vendedor na página
st.sidebar.title('Filtro por Vendedor(es)')
filtro_vendedor = st.sidebar.multiselect(
   'Vendedores',
   df['Vendedor'].unique() #valor unico de cada vendedor
)
if filtro_vendedor:
   df=df[df['Vendedor'].isin(filtro_vendedor)]

#criação de abas na pagina
aba1, aba2, aba3 = st.tabs(['Dataset', 'Receita', 'Vendedores'])
# enquanto estiver na aba1:
with aba1:
    st.dataframe(df)
#enquanto estiver na aba2:
with aba2:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
     st.metric('Receita Total (R$)', format_number(df['Preço'].sum(), 'R$'))
     st.plotly_chart(plotMapEstado, use_container_width=True)
     st.plotly_chart(plotReceitaEstado, use_container_width=True)   
    with coluna2:
     st.metric('Quantidade de Vendas', format_number(df.shape[0])) #que se inicia com indice 0
     st.plotly_chart(plotLinePrecoMensal, use_container_width=True)
     st.plotly_chart(plotReceitaCategoria, use_container_width=True)
with aba3:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
       st.plotly_chart(plotReceitaVendedor)
    with coluna2:
       st.plotly_chart(plotVendasVendedor)

#adição de filtros por coluna na página
st.sidebar.title('Filtro colunas')
with st.sidebar.expander('Colunas'):
   colunas=st.multiselect(
      'Selecione as Colunas',
      list(df.columns),
      list(df.columns)
   )

#adição de filtros por linha na página
st.sidebar.title('Filtros linha')
with st.sidebar.expander('Categoria do Produto'):
    categorias = st.multiselect(
       'Selecione as categorias',
       df['Categoria do Produto'].unique(),
       df['Categoria do Produto'].unique()
        )
with st.sidebar.expander('Preço do Produto'):
    preco = st.slider(
       'Selecione o preço',
       0,5000,
       (0,5000)
    )
with st.sidebar.expander('Data da compra'):
    data_compra = st.date_input(
       'Selecione a data',
       (df['Data da Compra'].min(),
       df['Data da Compra'].max())
    )

#queries
query = '''
    `Categoria do Produto` in @categorias and \
    @preco[0] <= Preço <= @preco[1] and \
    @data_compra[0] <= `Data da Compra`<= @data_compra[1]
'''
filtro_dados = df.query(query)
filtro_dados = filtro_dados[colunas]
st.dataframe(filtro_dados)
