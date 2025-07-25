from db_connection import connect
from usuarios_locales import usuarios
import bcrypt

""" 
Script para insertar usuarios iniciales en la base de datos. 
Este script se conecta a la base de datos y registra usuarios con sus roles correspondientes.
Se crean en base a un listado de usuarios predefinido en el archivo usuarios_locales.py.

"""


def insertar_usuario(nombre, username, password, rol, es_invitado=False):
    connection = connect()
    if connection is None:
        print("❌ Conexión fallida.")
        return

    try:
        cursor = connection.cursor()

        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        cursor.execute("""
            INSERT INTO usuarios (nombre, username, password, rol, es_invitado)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (username) DO NOTHING;
        """, (nombre, username, hashed.decode('utf-8'), rol, es_invitado))

        connection.commit()
        cursor.close()
        connection.close()
        print(f"✅ Usuario '{username},{rol}' insertado.")

    except Exception as e:
        print(f"❌ Error insertando usuario '{username}': {e}")

if __name__ == "__main__":
    for u in usuarios:
        insertar_usuario(
            u["nombre"],
            u["username"],
            u["password"],
            u["rol"],
            u.get("es_invitado", False)
        )
