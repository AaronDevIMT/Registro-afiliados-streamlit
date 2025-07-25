from db_connection import connect

"""
Script para crear todas las tablas del sistema.
Lee las instrucciones SQL desde un archivo externo para facilitar el mantenimiento.
"""

def crear_tablas():
    connection = connect()

    if connection is None:
        print("❌ No se pudo establecer conexión.")
        return

    try:
        cursor = connection.cursor()

        # Leer el archivo .sql externo
        with open("estructura.sql", "r", encoding="utf-8") as f:
            sql = f.read()

        cursor.execute(sql)
        connection.commit()
        cursor.close()
        connection.close()
        print("✅ Todas las tablas fueron creadas correctamente (si no existían).")

    except Exception as e:
        print(f"❌ Error al crear las tablas: {e}")

if __name__ == "__main__":
    crear_tablas()
