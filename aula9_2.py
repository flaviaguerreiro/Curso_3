import streamlit as st
import pandas as pd

st.title('LOCALIZAÇÃO DAS COMUNIDADES QUILOMBOLAS (2022)')
df = pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')

#limpando e organizando os dados
df.drop(columns=['Unnamed: 0'], inplace=True)


#convertendo latitude e longitude em número
list = ['Lat_d', 'Long_d']
df[list] =df[list].apply(pd.to_numeric, errors='coerce')

#criando lista com cada estado aparecendo uma única vez
estados = df['NM_UF'].unique().sort()

#inserindo caixa para seleção do estado 
estado_filtro = st.selectbox('Selecione o Estado:', estados)

#criando filtro para possibilitar a seleção dos dados de cada estado
dados_filtrados = df[df['NM_UF'] == estado_filtro]

#inserindo botão que permite exibir ou não a tabela de dados
if st.checkbox('Mostrar Tabela'):
  st.write(dados_filtrados)

#inserindo o mapa a partir da variável dados_filtrados
st.map(dados_filtrados, latitude='Lat_d', longitude='Long_d')


