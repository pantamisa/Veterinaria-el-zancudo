class Animal():
    def __init__(self, edad:str, nombreDueño: str, nombreAnimal: str, genero: str):
        self.edad = edad
        self.nombreDueño = nombreDueño
        self.genero = genero
        self.nombreAnimal = nombreAnimal
        
    def getnombreAnimal(self) -> str:
        print("Nombre Animal:", self.nombreAnimal)
        
    def getnombreDueño(self) -> str:
        print("Nombre Dueño:", self.nombreDueño)
        
    def getedadAnimal(self) -> str:
        print("Edad:", self.edad)
        
    def getgeneroAnimal(self) -> str:
        print("Nombre Animal:", self.genero)

class Perro(Animal):
    def __init__(self, edad: str, nombreDueño: str, nombreAnimal: str, genero: str, razaP: str):
        super().__init__(edad, nombreDueño, nombreAnimal, genero)
        self.razaP = razaP

    def getRaza(self) -> str:
        print("Raza Perro:", self.razaP)

    def setRaza(self, raza: str) -> None:
        self.razaP = raza


class Gato(Animal):
    def __init__(self, edad: str, nombreDueño: str, nombreAnimal: str, genero: str, razaG: str):
        super().__init__(edad, nombreDueño, nombreAnimal, genero)
        self.razaG = razaG

    def getRaza(self) -> str:
        print("Raza Gato:", self.razaG)

    def setRaza(self, raza: str) -> None:
        self.razaG = raza

class Ave(Animal):
    def __init__(self, edad: str, nombreDueño: str, nombreAnimal: str, genero: str, tipo: str):
        super().__init__(edad, nombreDueño, nombreAnimal, genero)
        self.tipo = tipo

    def getRaza(self) -> str:  
        print("Tipo de Ave:", self.tipo)

    def setRaza(self, tipo: str) -> None:
        self.tipo = tipo

#Ejemplo salida
perro1 = Perro("5", "Carlos", "Firulais", "M", "Labrador")
perro1.getnombreAnimal()
perro1.getRaza()

gato1 = Gato("3", "Ana", "Michi", "F", "Siames")
gato1.getnombreAnimal()
gato1.getRaza()

ave1 = Ave("2", "Laura", "Piolín", "M", "Canario")
ave1.getnombreAnimal()
ave1.getRaza()