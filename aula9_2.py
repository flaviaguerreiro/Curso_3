import streamlit as st
import pandas as pd

st.title('LOCALIZAÇÃO DAS COMUNIDADES QUILOMBOLAS (2022)')
df = pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')

#limpando e organizando os dados
df.drop(columns=['Unnamed: 0'], inplace=True)
df = df.sort_values(by='NM_UF')

#convertendo latitude e longitude em número
list = ['Lat_d', 'Long_d']
df[list] =df[list].apply(pd.to_numeric, errors='coerce')

#criando lista com cada estado aparecendo uma única vez
estados = df['NM_UF'].unique()

#inserindo caixa para seleção do estado 
estado_filtro = st.selectbox('Selecione o Estado:', estados)

#criando filtro para possibilitar a seleção dos dados de cada estado
dados_filtrados = df[df['NM_UF'] == estado_filtro]

#inserindo botão que permite exibir ou não a tabela de dados
if st.checkbox('Mostrar Tabela'):
  st.write(dados_filtrados)

#inserindo o mapa a partir da variável dados_filtrados
st.map(dados_filtrados, latitude='Lat_d', longitude='Long_d')

qtdeMunicipios = len(df['NM_MUNIC'].unique())
st.write("A quantidade de municípios com localização quilombola é " + str(qtdeMunicipios))

qtdeComunidades = len(df['NM_AGLOM'].unique())
st.write("A quantidade de comunidades quilombolas é " + str(qtdeComunidades))

st.header('Número de comunidades por UF')
st.bar_chart(df['NM_UF'].value_counts())

st.header('Os dez municípios com mais comunidades quilombolas')
st.bar_chart(df['NM_MUNIC'].value_counts()[:10])

numero = st.slider('Selecione um número de linhas a serem exibidas', min_value = 0, max_value = 100)
st.write(df.head(numero))
