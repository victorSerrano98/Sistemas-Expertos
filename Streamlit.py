import time
from time import sleep
import streamlit
import streamlit as st
import pandas as pd


### Encabezado ###
import SE

st.set_page_config(page_title="Sistemas Expertos")
st.markdown('___')
st.markdown("<h4 style='text-align: center; color:grey;'>Universidad Nacional de Loja</h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color:grey;'>Ingeniería en Sistemas</h4>", unsafe_allow_html=True)
st.markdown(
    "<h1 style='text-align: center; color:Black;frameborder=1;'>""Sistema experto para la recomendacion de plantas medicinales""</h1>",
    unsafe_allow_html=True)
# ![Star (https://unl.edu.ec/sites/default/files/inline-images/logo_0.png?style=social)](https://unl.edu.ec/)

st.markdown('___')


######

def classify(num):
    if num == 0:
        return 'setosa'
    else:
        return 'virginica'


def main():

    def parametros():
        pregunta = st.text_input('¿Cual es su sintoma?')

        return pregunta


    pregunta = parametros()
    if st.button('Enviar pregunta'):
        respuesta = SE.consulta(pregunta)
        # print(articulos)
        if(len(respuesta)>1):
            st.success(respuesta)
        else:
            st.error("No se encontraron respuestas")

    st.markdown('___')

if __name__ == '__main__':
    main()