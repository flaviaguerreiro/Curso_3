import streamlit as st
import pandas as pd

df = pd.DataFrame({'nome_Servifor': ['Adriana', 'Mônica', 'Samara'], 
                   'Salário': [1200, 300, 5000]})

st.write('Crinando uma tabela!')
st.write(df)
