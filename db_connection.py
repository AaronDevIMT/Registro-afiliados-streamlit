# db_connection.py
# ---------------------------------------------
# Este módulo se encarga de establecer una conexión
# con una base de datos PostgreSQL (como Supabase).
# Utiliza variables de entorno para proteger las credenciales.
# ---------------------------------------------

import os
import psycopg2              # Librería para conectar Python con PostgreSQL
from dotenv import load_dotenv  # Para cargar variables desde un archivo .env

try:
    import streamlit as st
    # Solo usar secrets si realmente existen y no están vacíos
    USE_STREAMLIT_SECRETS = False
    if hasattr(st, "secrets"):
        try:
            USE_STREAMLIT_SECRETS = bool(st.secrets)
        except Exception:
            USE_STREAMLIT_SECRETS = False
except ImportError:
    USE_STREAMLIT_SECRETS = False

# Cargar las variables definidas en el archivo .env
load_dotenv()

def get_db_config():
    if USE_STREAMLIT_SECRETS:
        return {
            "user": st.secrets["user"],
            "password": st.secrets["password"],
            "host": st.secrets["host"],
            "port": st.secrets["port"],
            "dbname": st.secrets["dbname"]
        }
    else:
        return {
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD"),
            "host": os.getenv("DB_HOST"),
            "port": os.getenv("DB_PORT"),
            "dbname": os.getenv("DB_NAME")
        }

def connect():
    """
    Establece una conexión con la base de datos PostgreSQL
    utilizando las credenciales almacenadas en variables de entorno.

    Retorna:
        - Objeto de conexión si fue exitosa.
        - None si ocurre algún error.
    """
    config = get_db_config()
    try:
        connection = psycopg2.connect(
            user=config["user"],             # Usuario de la base de datos
            password=config["password"],     # Contraseña del usuario
            host=config["host"],             # Dirección del servidor (host)
            port=config["port"],             # Puerto de conexión (generalmente 5432)
            dbname=config["dbname"],         # Nombre de la base de datos
            sslmode="require"                # Requerido por Supabase para conexión segura
        )
        return connection

    except Exception as e:
        print(f"❌ Error al conectar a la base de datos: {e}")
        return None

if __name__ == "__main__":
    conn = connect()
    if conn:
        print("✅ Conexión exitosa a la base de datos.")
        conn.close()
    else:
        print("❌ No se pudo establecer conexión a la base de datos.")