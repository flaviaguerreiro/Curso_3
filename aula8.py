import streamlit as st
st.write("Hello World")
st.title('Este é o título do app')
st.header('Este é o subtítulo')
st.subheader('Este é o terceiro subtítulo')
st.markdown('Este é o texto')
st.caption('ESta é a legenda')
st.code('x=2021')
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

#questão 3
# Código 1
escala= list(range(101))
satisfacao = st.select_slider('Satisfação do Cliente', options=escala)
st.write(f'Valor Selecionado: {satisfacao}')

#Código 2
satisfacao = st.slider('Satisfação do Cliente', min_value = 0, max_value = 100)
st.text('Valor Selecionado:'+str(satisfacao))

#questão 4
# criando elementos gráficos
x = st.checkbox('Sim')
st.write(x)

# fazer o mesmo com alguns dos comandos abaixo
st.title(x)
st.button('Clique')
st.radio('Selecione seu gênero',['Masculino','Feminino'])
st.selectbox('Selecione seu gênero',['Masculino','Feminino'])
st.multiselect('Escolha um departamento',['DCS', 'DE', 'DIR'])
st.select_slider('Selecione uma resposta', ['Ruim', 'Bom', 'Excelente'])
st.slider('Selecione um número', 0,50)
st.number_input('Selecione um número', 0,10)
st.text_input('Endereço de e-mail')
st.date_input('Data de viagem')
st.time_input('Tempo de escola')
st.text_area('Descrição')
st.file_uploader('Atualize uma foto')
st.color_picker('Escolha sua cor favorita')

# mensagens de status
st.success("Você conseguiu!")
st.error("Erro!")
st.warning("Advertência")
st.info("Esta é uma informação")
