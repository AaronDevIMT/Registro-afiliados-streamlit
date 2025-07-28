# 📋 Registro de Afiliados – Streamlit App

![Captura de la app](assets/preview.png)

Aplicación web desarrollada con **Python + Streamlit + PostgreSQL** que permite a promotores gestionar registros de afiliados de manera intuitiva, rápida y desde cualquier dispositivo. Esta herramienta fue diseñada con el objetivo de modernizar procesos de afiliación manual y facilitar el control de datos de manera descentralizada pero segura.

📝 Este proyecto fue originalmente desarrollado como una **solicitud de un cliente**, quien requería un sistema capaz de crear y mantener una base de datos de afiliados mediante formularios en línea, con actualización en tiempo real. Posteriormente, se le añadió un **modo invitado** con el objetivo de incluirlo como parte de mi portafolio profesional. También ha sido usado como **beta demostrativa** para otro cliente (un nutriólogo), que buscaba un sistema similar para registrar información de sus pacientes vía web.

---

## 🚀 Funcionalidades principales

- 🔐 Inicio de sesión por usuario registrado o como invitado  
- 🧑‍💼 CRUD completo de afiliados  
- 🗃️ Separación de tablas por promotor con sincronización a tabla general  
- 📝 Registro de historial de cambios mediante triggers SQL  
- 📆 Control de asistencias a reuniones  
- 🔍 Interfaz rápida, sencilla y adaptable a móviles  

---

## 🛠️ Tecnologías utilizadas

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.27-red)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)
![Git](https://img.shields.io/badge/Git-Control-lightgrey)

---

## 🧑‍💻 Cómo ejecutar localmente

### 1. Clona el repositorio:

```bash
git clone https://github.com/AaronDevIMT/Registro-afiliados-streamlit.git
cd Registro-afiliados-streamlit
```

### 2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

### 3. Configura tus variables de entorno

Puedes usar un archivo `.env` o configurar los `secrets.toml` de Streamlit.

Ejemplo `.env`:

```env
DB_HOST=localhost
DB_NAME=afiliados
DB_USER=postgres
DB_PASSWORD=tu_contraseña_segura
```

### 4. Ejecuta la app:

```bash
streamlit run main.py
```

---

## 🌐 Demo en línea

Puedes ver la app funcionando aquí:  
👉 **[registro-afiliados.streamlit.app](https://registro-afiliados.streamlit.app/)**

---

## 🧠 Aprendizajes

Este proyecto fue una oportunidad para aplicar y consolidar conocimientos sobre:

- Manejo de bases de datos relacionales y relaciones N:M  
- Seguridad en despliegue en Streamlit Cloud  
- Separación de lógica backend en módulos Python  
- Diseño de interfaces simples con Streamlit  

---

## 📬 Contacto  

<p align="center">
  <strong>Aarón Águilar May</strong>  
  <br><br>
  [![Email](https://img.shields.io/badge/Email-aaron.agm02%40gmail.com-red?logo=gmail&logoColor=white)](mailto:aaron.agm02@gmail.com)  
  📧 **Copiar y pegar:** `aaron.agm02@gmail.com`  
  <br><br>
  🐙 <a href="https://github.com/AaronDevIMT">GitHub – AaronDevIMT</a>  
</p>

---

## 🧾 Licencia

MIT License – libre para uso educativo y personal.
