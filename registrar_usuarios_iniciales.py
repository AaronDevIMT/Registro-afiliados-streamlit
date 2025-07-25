from db_connection import connect
import bcrypt
from usuarios_locales import usuarios
"""
    Script para insertar usuarios iniciales en la base de datos.

"""

def insertar_usuario(username, password, rol, es_invitado=False):
    connection = connect()
    if connection is None:
        print("❌ Conexión fallida.")
        return
    
    try:
        cursor = connection.cursor()
        # Encriptar la contraseña
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        cursor.execute("""
            INSERT INTO usuarios (username, password, rol, es_invitado)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (username) DO NOTHING;
        """, (username, hashed.decode('utf-8'), rol, es_invitado))

        connection.commit()
        cursor.close()
        connection.close()
        print(f"✅ Usuario '{username}' '{rol}' registrado correctamente.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    for u in usuarios:
        insertar_usuario(u["username"], u["password"], u["rol"], u.get("es_invitado", False))