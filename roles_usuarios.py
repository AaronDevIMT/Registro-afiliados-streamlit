# roles_usuarios.py
# --------------------
# Clases para representar roles del sistema WEB_REGISTRO
# Cada clase define qué operaciones puede ejecutar un tipo de usuario.

from db_connection import connect
import streamlit as st

class Usuario:
    def __init__(self, usuario_id, username):
        self.usuario_id = usuario_id
        self.username = username

    def ver_mensaje_bienvenida(self):
        st.markdown(
            f"""
            <div style='display: flex; align-items: center; gap: 10px;'>
                <span style='font-weight: bold;'>Sesión activa:</span>
                <span style='background-color: #27ae60; color: white; padding: 6px 16px; border-radius: 8px; font-weight: bold;'>
                    {self.username}
                </span>
                <span style='color: #27ae60; font-size: 1.5em;'>&#9679;</span>
            </div>
            """,
            unsafe_allow_html=True
        )


class Colaborador(Usuario):
    def registrar_afiliado(self, nombre, apellido, domicilio, celular, seccion, municipio, promotor_id):
        conn = connect()
        if not conn:
            st.error("Error de conexión")
            return
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO afiliados (nombre, apellido, domicilio, celular, seccion, municipio, promotor_id, usuario_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (nombre, apellido, domicilio, celular, seccion, municipio, promotor_id, self.usuario_id))
            conn.commit()
            st.success("Afiliado registrado correctamente.")
        except Exception as e:
            st.error(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    def ver_afiliados(self):
        conn = connect()
        if not conn:
            st.error("Error de conexión")
            return []
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM afiliados WHERE usuario_id = %s ORDER BY afiliado_id DESC", (self.usuario_id,))
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            st.error(f"Error: {e}")
            return []
        finally:
            cursor.close()
            conn.close()

    def editar_afiliado(self, afiliado_id, nuevo_dato, campo):
        conn = connect()
        if not conn:
            st.error("Error de conexión")
            return
        cursor = conn.cursor()
        try:
# Verificar si el afiliado existe y pertenece al usuario
            cursor.execute(
                "SELECT 1 FROM afiliados WHERE afiliado_id = %s AND promotor_id = %s",
                (afiliado_id, self.usuario_id)
            )
            existe = cursor.fetchone()
            if not existe:
                st.warning("El afiliado no existe o no tienes permisos para editarlo.")
                return

            sql = f"UPDATE afiliados SET {campo} = %s WHERE afiliado_id = %s AND promotor_id = %s"
            cursor.execute(sql, (nuevo_dato, afiliado_id, self.usuario_id))
            conn.commit()
            st.success("Afiliado actualizado.")
        except Exception as e:
            st.error(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()


class Admin(Colaborador):
    def eliminar_afiliado(self, afiliado_id):
        conn = connect()
        if not conn:
            st.error("Error de conexión")
            return
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM afiliados WHERE afiliado_id = %s", (afiliado_id,))
            conn.commit()
            st.success("Afiliado eliminado correctamente.")
        except Exception as e:
            st.error(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    def ver_todos_afiliados(self):
        conn = connect()
        if not conn:
            st.error("Error de conexión")
            return []
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM afiliados ORDER BY afiliado_id DESC")
            return cursor.fetchall()
        except Exception as e:
            st.error(f"Error: {e}")
            return []
        finally:
            cursor.close()
            conn.close()

    def agregar_promotor(self, nombre, apellido, domicilio, celular, seccion, municipio):
        """
        Agrega un nuevo promotor a la tabla promotores.
        """
        conn = connect()
        if not conn:
            st.error("Error de conexión")
            return
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO promotores (nombre, apellido, domicilio, celular, seccion, municipio)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (nombre, apellido, domicilio, celular, seccion, municipio))
            conn.commit()
            st.success("Promotor agregado correctamente.")
        except Exception as e:
            st.error(f"Error al agregar promotor: {e}")
        finally:
            cursor.close()
            conn.close()

    def obtener_promotores():
        conn = connect()
        if not conn:
            st.error("No se pudo conectar a la base de datos para cargar promotores.")
            return []
        cursor = conn.cursor()
        cursor.execute("SELECT promotor_id, nombre FROM promotores ORDER BY nombre")
        promotores = cursor.fetchall()
        cursor.close()
        conn.close()
        return promotores

    def ver_promotores():
        conn = connect()
        if not conn:
            return []
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM promotores ORDER BY promotor_id DESC")
        promotores = cursor.fetchall()
        cursor.close()
        conn.close()
        return promotores

class Invitado(Colaborador):
    def registrar_afiliado(self, nombre, apellido, domicilio, celular, seccion, municipio, promotor_id):
        st.info("[Demo] Afiliado simulado como registrado (no se guardó en base de datos).")

    def editar_afiliado(self, afiliado_id, nuevo_dato, campo):
        st.warning("[Demo] No se realizan cambios reales.")

    def ver_afiliados(self):
        st.info("[Demo] Mostrando afiliados simulados.")
        return []
