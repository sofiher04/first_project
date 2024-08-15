import streamlit as st
from PIL import Image

st.title("Regaste tu planta ☘️")

st.header('Si fueras una planta...')
st.write('¿Qué planta serías?')
iamge = Image.open('plants.jpg')
st.image(image, camption = '¡Yo soy todas las plantas!')
texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto)
st.subheader("Ahora usemos 2 columna")
