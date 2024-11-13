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
escala= list(range(101))
satisfacao = st.select_slider('Satisfação do Cliente', options=escala)
st.write(f'Valor Selecionado: {satisfacao}')

satisfacao = st.slider('Satisfação do Cliente', min_value = 0, max_value = 100)
st.text('Valor Selecionado:'+str(satisfacao))

#questão 4
