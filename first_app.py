import streamlit as st
from PIL import Image

st.title("Regaste tu planta ☘️")

st.header('Si fueras una planta...')
st.write('¿Qué planta serías?')
image = Image.open('plants.jpg')

st.image(image, caption = '¡Yo soy todas las plantas!')

texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto)
