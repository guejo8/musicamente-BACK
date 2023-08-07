
Este es el repositorio backend del proyecto fullstack Musicamente school, ha sido desarrollado utilizando Python y se conecta con una base de datos MongoDB alojada en MongoDB Atlas.
Proporciona una API REST para que el frontend y otros clientes accedan y manipulen la información de las lecciones


1.Crear un entorno virtual

python -m venv venv or python3 -m venv .venv

2. Activar el entorno virtual:
----en macOS o Linux:----

. .venv/bin/activate or source venv/bin/activate

----en Windows:----

.venv\Scripts\activate

3. Una vez activado el entorno:

pip install -r requirements.txt

4. Arrancar el proyecto:

python app.py o python3 app.py


Para la base de datos:

1. Crear  database en Mongodb Atlas y/o Mongodb Compass

2. Importar el contenido de la carpeta copia bd incluida en este proyecto

3. Cambiar la uri para la conexion en app.py
