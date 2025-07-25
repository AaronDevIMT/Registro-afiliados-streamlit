# login_usuario.py

import streamlit as st
import bcrypt
from db_connection import connect
from roles_usuarios import Admin, Colaborador, Invitado

""""
Script para manejar el inicio de sesión de usuarios en la aplicación WEB_REGISTRO.
Define las funciones para autenticar usuarios y mostrar el formulario de inicio de sesión.

"""
def autenticar(username, password):
    conn = connect()
    if not conn:
        st.error("No se pudo conectar a la base de datos.")
        return None

    cursor = conn.cursor()
    cursor.execute("SELECT usuario_id, username, password, rol FROM usuarios WHERE username = %s", (username,))
    resultado = cursor.fetchone()
    cursor.close()
    conn.close()

    if resultado:
        user_id, username_db, hash_db, rol = resultado
        if bcrypt.checkpw(password.encode(), hash_db.encode()):
            if rol == "admin":
                return Admin(user_id, username_db)
            elif rol == "colaborador":
                return Colaborador(user_id, username_db)
            else:
                return Invitado(user_id, username_db)
    return None


def mostrar_login():
    st.title("Inicio de Sesión")

    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    col1, col2 = st.columns([3, 1])
    with col1:
        if st.button("Iniciar sesión"):
            usuario = autenticar(username, password)
            if usuario:
                st.session_state["logueado"] = True
                st.session_state["usuario"] = usuario
                st.success(f"Bienvenido {usuario.username}")
                st.rerun()
            else:
                st.error("Usuario o contraseña incorrectos.")

    with col2:
        if st.button("Invitado"):
            st.session_state["logueado"] = True
            st.session_state["usuario"] = Invitado(None, "Invitado")
            st.rerun()

if __name__ == "__main__":
    mostrar_login()