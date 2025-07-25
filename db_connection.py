# db_connection.py
# ---------------------------------------------
# Este módulo se encarga de establecer una conexión
# con una base de datos PostgreSQL (como Supabase).
# Utiliza variables de entorno para proteger las credenciales.
# ---------------------------------------------

import psycopg2              # Librería para conectar Python con PostgreSQL
from dotenv import load_dotenv  # Para cargar variables desde un archivo .env
import streamlit as st       # Acceder a las variables secretas de streamlit

# Cargar las variables definidas en el archivo .env
load_dotenv()
print("Host desde .env:", st.secrets["host"])


def connect():
    """
    Establece una conexión con la base de datos PostgreSQL
    utilizando las credenciales almacenadas en variables de entorno.

    Retorna:
        - Objeto de conexión si fue exitosa.
        - None si ocurre algún error.
    """
    try:
        connection = psycopg2.connect(
            user=st.secrets["user"],             # Usuario de la base de datos
            password=st.secrets["password"],     # Contraseña del usuario
            host=st.secrets["host"],             # Dirección del servidor (host)
            port=st.secrets["port"],             # Puerto de conexión (generalmente 5432)
            dbname=st.secrets["dbname"],         # Nombre de la base de datos
            sslmode="require"                    # Requerido por Supabase para conexión segura
        )
        return connection

    except Exception as e:
        print(f"❌ Error al conectar a la base de datos: {e}")
        return None

if __name__ == "__main__":
    # Prueba de conexión al ejecutar este script directamente
    conn = connect()
    if conn:
        print("✅ Conexión exitosa a la base de datos.")
        conn.close()  # Cerrar la conexión si fue exitosa
    else:
        print("❌ No se pudo establecer conexión a la base de datos.")