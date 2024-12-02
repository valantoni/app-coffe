import streamlit as st

st.set_page_config(page_title="Coffe shop", page_icon="☕", layout="centered")

st.write("##")
st.title("¡Unete a la familia de cafeteros!")

c1,c2 = st.columns(2)
with c1:
    st.write("##")
    st.image("assets/logo.png")
with c2:
    st.write("##")
    nombre = st.text_input("Nombre*", placeholder="Tu nombre")
    email = st.text_input("Email*", placeholder="Tu mejor email")
    fecha_nacimiento = st.date_input("Fecha de nacimiento", help="Tu cumpleaños es importante para nosotros, te enviaremos un regalo especial ! 😉", value=None)
    policy = st.checkbox("Acepto recibir emails por parte de la empresa")

    enviar = st.button("Enviar ☕")

st.write("##")
st.caption("© 2021 Coffe shop. Todos los derechos reservados")