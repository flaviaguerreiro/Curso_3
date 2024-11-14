import streamlit as st
import pandas as pd

st.title('LOCALIZAÇÃO DAS COMUNIDADES QUILOMBOLAS (2022)')
df = pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')

df.drop(columns=['Unnamed: 0'], inplace=True)

#convertendo latitude e longitude em número
list = ['Lat_d', 'Long_d']
df[list] =df[list].apply(pd.to_numeric, errors='coerce')

#criando lista com cada estado aparecendo uma única vez
estados = df['NM_UF'].unique()
estado_filtro = st.selectbox('Selecione o Estado:', estados)

