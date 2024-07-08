from abc import ABC, abstractmethod

class Animal(ABC):
    patas = 4
    @abstractmethod
    def moverse(self):
        pass
    
class Perro(Animal):
    def moverse(self):
        print("El perro corretea")
        
    def ladrar(self):
        print("El perro ladra guau guau!")
        
class Gato(Animal):
    def moverse(self):
        print("El perro corretea")
        
    def maullar(self):
        print("El perro ladra miau miau!")
        
inst = Gato()