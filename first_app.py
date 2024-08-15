import streamlit as st
from PIL import Image

st.title("Regaste tu planta ☘️")

st.header('Si fueras una planta...')
st.write('¿Qué planta serías?')
image = Image.open('plants.jpg')

st.image(image, caption = '¡Yo soy todas las plantas!')

texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es: ', texto)

st.subheader("Ahora usemos 2 columnas")
col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las plantas de interior mejoran tu ánimo")
  resp = st.checkbox('Así es')
  if resp:
    st.write('¡Correcto!')

with col2:
  st.subheader("Esta es la segunda columna")
  modo = st.radio("¿Cuál planta de inerior te gusta más?", ('Lirio de la paz', 'Guzmania mini rosa', 'Árbol de jade', 'Aloe vera'))
  if modo == 'Lirio de la paz':
    st.write('Se trata de una planta que purifica de forma natural y que desprende elegancia. Una de las pocas que, estando en interior, son capaces de florecer durante todo el año.')
  if modo == 'Guzmania mini rosa':
    st.write('Su tamaño es ideal para lucirla en cualquier espacio pequeño de la casa, sobre todo, en esos rincones a los que le falta ese toque alegre.')
  if modo == 'Árbol de jade':
    st.write('Una de las plantas suculentas más conocidas del mundo, con sus hojas carnosas y su forma de pequeño arbolito.')
  if modo == 'Aloe vera':
    st.write('Además de ser súper vistoso, sus hojas pueden ser utilizadas con fines terapéuticos y de belleza Será bueno que le dé la luz siempre que sea posible, pero tan solo has de regar cada 15 o 20 días con poquita agua.')

st.subheader('Uso de Botones')
st.write('¡Presiona la planta!')
if st.button('🌱'):
  st.write("Gracias por presionar :)")
else:
  st.write('No has presionado nada :(')

with st.sidebar:
st.subheader('Configura la modalidad')
mod_radio = st.radio("Escoge la modalidada a usar", ("Visual", "Auditiva", "Háptica"))
