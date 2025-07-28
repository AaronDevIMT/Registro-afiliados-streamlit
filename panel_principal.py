# panel_principal.py

import streamlit as st
from roles_usuarios import Admin
import pandas as pd


def mostrar_panel(usuario):
    usuario.ver_mensaje_bienvenida()

    opciones = ["Registrar afiliado", "Ver afiliados", "Editar afiliado"]
    if isinstance(usuario, Admin):
        opciones.append("Eliminar afiliado")
        opciones.append("Ver todos los afiliados")
        opciones.append("Agregar promotor")
        opciones.append("Ver promotores") 

    seleccion = st.sidebar.radio("Selecciona una acción", opciones)

    if seleccion == "Registrar afiliado":
        # Obtener promotores para la lista desplegable
        promotores = Admin.obtener_promotores()
        promotor_opciones = [f"{p[0]} - {p[1]}" for p in promotores]
        with st.form("registro"):
            nombre = st.text_input("Nombre")
            apellido = st.text_input("Apellido")
            domicilio = st.text_input("Domicilio")
            celular = st.text_input("Celular")
            seccion = st.text_input("Sección")
            municipio = st.text_input("Municipio")
            promotor_seleccionado = st.selectbox("Promotor", promotor_opciones)
            enviar = st.form_submit_button("Guardar")
            if enviar:
                promotor_id = int(promotor_seleccionado.split(" - ")[0])
                usuario.registrar_afiliado(nombre, apellido, domicilio, celular, seccion, municipio, promotor_id)

    elif seleccion == "Agregar promotor" and isinstance(usuario, Admin):
        with st.form("agregar_promotor"):
            nombre = st.text_input("Nombre del promotor")
            apellido = st.text_input("Apellido del promotor")
            domicilio = st.text_input("Domicilio")
            celular = st.text_input("Celular")
            seccion = st.text_input("Sección")
            municipio = st.text_input("Municipio")
            enviar = st.form_submit_button("Agregar promotor")
            if enviar:
                usuario.agregar_promotor(nombre, apellido, domicilio, celular, seccion, municipio)

    elif seleccion == "Ver promotores" and isinstance(usuario, Admin):
        promotores = Admin.ver_promotores()
        if promotores:
            df = pd.DataFrame(promotores, columns=["ID", "Nombre", "Apellido", "Domicilio", "Celular", "Sección", "Municipio"])
            st.dataframe(df[["ID", "Nombre", "Apellido", "Domicilio", "Celular", "Sección", "Municipio"]], use_container_width=True, hide_index=True)
        else:
            st.info("No hay promotores registrados.")

    elif seleccion == "Ver afiliados":
        afiliados = usuario.ver_afiliados()
        if afiliados:
            df = pd.DataFrame(afiliados, columns=["ID", "Nombre", "Apellido", "Domicilio", "Celular", "Sección", "Municipio", "Promotor ID"])
            st.dataframe(df[["ID", "Nombre", "Apellido", "Domicilio", "Celular", "Sección", "Municipio"]], use_container_width=True, hide_index=True)
        else:
            st.info("No hay afiliados registrados.")

    elif seleccion == "Editar afiliado":
        afiliado_id = st.number_input("ID del afiliado a editar", min_value=1, step=1)
        campo = st.selectbox("Campo a modificar", ["domicilio", "celular"])
        nuevo_valor = st.text_input("Nuevo valor")
        if st.button("Actualizar"):
            usuario.editar_afiliado(afiliado_id, nuevo_valor, campo)

    elif seleccion == "Eliminar afiliado" and isinstance(usuario, Admin):
        afiliado_id = st.number_input("ID del afiliado a eliminar", min_value=1, step=1)
        if st.button("Eliminar"):
            usuario.eliminar_afiliado(afiliado_id)

    elif seleccion == "Ver todos los afiliados" and isinstance(usuario, Admin):
        afiliados = usuario.ver_todos_afiliados()
        if afiliados:
            df = pd.DataFrame(afiliados, columns=["ID", "Nombre", "Apellido", "Domicilio", "Celular", "Sección", "Municipio", "Promotor ID", "Usuario ID"])
            st.dataframe(df[["ID", "Nombre", "Apellido", "Domicilio", "Celular", "Sección", "Municipio"]], use_container_width=True, hide_index=True)
        else:
            st.info("No hay afiliados registrados.")
