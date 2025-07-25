import streamlit as st
from login_streamlit import mostrar_login
from panel_principal import mostrar_panel

if "logueado" not in st.session_state:
    st.session_state["logueado"] = False
    st.session_state["usuario"] = None

if st.session_state["logueado"]:
    mostrar_panel(st.session_state["usuario"])
else:
    mostrar_login()
