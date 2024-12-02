import streamlit as st
import re
from google_sheets import GoogleSheet
import uuid
from datetime import datetime

##VARIABLES##
credentials = st.secrets["google"]["credentials_google"]
document_name = "bbdd-app-email-marketing"
sheet_name = "contactos"

##FUNCIONES##
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False

def generate_unique_id():
    return str(uuid.uuid4())

##FRONT##
st.set_page_config(page_title="Coffe shop", page_icon="☕", layout="centered")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            
            
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

hide_github_icon = """
#GithubIcon {
  visibility: hidden;
}
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)

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

##BACK##
    if enviar:
        if not nombre:
            st.error("Por favor, completa el campo del nombre")
        elif not email:
            st.error("Por favor, completa el campo del email")
        elif not validate_email(email):
            st.error("Por favor, ingresa un email válido")    
        elif not policy:
            st.error("Por favor, acepta la política de privacidad")
        elif fecha_nacimiento is not None and fecha_nacimiento > datetime.now().date():
            st.error("Por favor, ingresa una fecha de nacimiento válida")
        else:
            try:
                with st.spinner("Guardando información..."):
                    uid = generate_unique_id()
                    timestamp = str(datetime.now())
                    values = [[uid,nombre,email,str(fecha_nacimiento),timestamp]]
                    gsheet = GoogleSheet(credentials,document_name,sheet_name)
                    range = gsheet.get_last_row_range()
                    gsheet.write_data(range,values)

                    st.success("¡Gracias por unirte a la familia de cafeteros! ")
            
            except Exception as e:
                st.error(f"Ocurrió un error al enviar su información")           
            
st.write("##")
st.caption("© 2021 Coffe shop. Todos los derechos reservados")