# SistemaReservasDjango
Sistema de reservas para el modulo 5 en Django
El proyecto de Django de reservas es una aplicación web que permite a los usuarios realizar reservas en hoteles. A continuación, se proporciona una descripción general de sus características principales:

Modelos: Hotel, Habitación, Cliente y Reserva. Estos modelos definirán los campos y relaciones necesarios para almacenar información sobre hoteles, habitaciones, clientes y reservas en la base de datos.

Vistas: Las vistas del proyecto serán responsables de procesar las solicitudes HTTP y generar respuestas. Pueden incluir vistas para mostrar la lista de hoteles, detalles de un hotel específico, disponibilidad de habitaciones, formulario de reserva, entre otros.


Pasos para ejecutar el sistema. 
1. Clonar el repositorio
2. Verificar las dependencias 
pip install -r requirements.txt
3. Configura la base de datos si lo desea desde settings.py
4. Realiza las migraciones de la base de datos 
python manage.py makemigrations
python manage.py migrate
5. Ejecuta el servidor de desarrollo
python manage.py runserver

Esto iniciará el servidor de desarrollo en http://localhost:8000

Instalar el proyecto usando un ambiente virtual de python
1. Crea un entorno virtual:
python -m venv myenv

2. Activa el entorno virtual:
En windos: myenv\Scripts\activate
En Mac/Linux: source myenv/bin/activate

3. Instala las dependencias del proyecto:
pip install -r requirements.txt

4. Realiza las migraciones de la base de datos
python manage.py migrate

5. Ejecuta el servidor de desarrollo
python manage.py runserver

Esto iniciará el servidor de desarrollo en http://127.0.0.1:8000/

Documentación si desea usar los Endpoints desde Postman
1. GET request: {habitaciones, reservas, clientes, hoteles}
curl --location 'http://127.0.0.1:8000/habitaciones' 

2. POST request:
curl --location 'http://127.0.0.1:8000/hoteles/' \
--header 'Content-Type: application/json' \
--data '{"nombre": "Hotel ABC", "direccion": "Ciudad XYZ"}'

3. OPTION request: 
curl --location --request OPTIONS 'http://127.0.0.1:8000/hoteles/'