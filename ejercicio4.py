# Crear una interfaz para conexion de base de datos y una clase para postgresql, mysql y oracle
 from abc import ABC, abstractmethod

class Database(ABC):
 @abstractmethod
 def connect(sel, host: str)

# * Se necesita una direccion, un usuario y una contraseña
 

# * Testear con tests, y hacer un metodo para todas que sea testear conexion (una especie de ping), sin necesidad de usuario o contraseña)