
# Entorno virtual
- python -m venv .venv

- .\.venv\Scripts\activate

- Instalamos los paquetes:  pip install -r .\requirements.txt

# Iniciado Projecto

- django-admin startproject weather_project
- cd .\weather_project\

# creamos una app dentro de la carpeta ya creada
- pyhton.exe .\manage.py startapp weather
  
# run el servidor
- python.exe .\manage.py runserver

## ERROR

- You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions. Run 'python manage.py migrate' to apply them.: 
- python manage.py migrate

![alt text](image-3.png)