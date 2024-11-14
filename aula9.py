import streamlit as st
import pandas as pd

df = pd.DataFrame({'nome_Servidor': ['Adriana', 'Mônica', 'Samara'], 
                   'Salário': [1200, 300, 5000]})

st.write('Crinando uma tabela!')
st.write(df)

opcao = st.selectbox('Qual servidor você gostariade selecionar?', df['nome_Servidor'])

st.write('Você selecionou: ', opcao)

dadosFiltrados = df[df['nome_Servidor'] == opcao]
dadosFiltrados
