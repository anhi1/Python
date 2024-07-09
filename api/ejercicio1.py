# crear un usuario
# python -m venv j-venv |   | pip install requests | pip install python-dotenv



import requests
 
url = "https://reqres.in/api/users"
data = requests.get(url).json()['data']
print(f"Nombre: {data['first_name']}, Apellido: {data['last_name']}")
 
 



# import os, pathlib
# from dotenv import load_dotenv
 
# _path = pathlib.Path(".").resolve()
# load_dotenv(_path / "secrets.env")
 
# google_password = os.getenv("password")