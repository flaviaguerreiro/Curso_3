import pandas as pd
import requests as req
import streamlit as st

#A partir dos dados abertos da camara dos deputados (https://dadosabertos.camara.leg.br/swagger/api.html) defina a URL da API com informações sobre os deputados, incluindo a informação sobre o gênero. DICA: Use a opção de deputados.
url_homens= 'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=M&ordem=ASC&ordenarPor=nome'
url_mulheres= 'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=F&ordem=ASC&ordenarPor=nome'

dados_homens= req.get(url_homens)
dados_mulheres= req.get(url_mulheres)

dfhomens = pd.DataFrame(dados_homens)
dfmulheres = pd.DataFrame(dados_mulheres)

df = pd.concat([dfhomens, dfmulheres])

st.title('DETADOS - DADOS POR SEXO')
opcoes =[f'{Masculino} - {Feminino}'for Masculino in dfhomens for Feminino in dfmulheres]
sexo = st.selectbox('Sexo:', opcoes)
