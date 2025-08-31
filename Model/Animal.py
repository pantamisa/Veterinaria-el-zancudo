class Animal():
    def __init__(self, edad:str, nombreDueño: str, nombreAnimal: str, genero: str):
        self.__edad = edad
        self.__nombreDueño = nombreDueño
        self.__genero = genero
        self.__nombreAnimal = nombreAnimal
        
    def getnombreAnimal(self) -> str:
        return self.__nombreAnimal
        
    def getnombreDueño(self) -> str:
        return "Nombre Dueño:", self.__nombreDueño
        
    def getedadAnimal(self) -> str:
        return "Edad:", self.__edad
        
    def getgeneroAnimal(self) -> str:
        return "Nombre Animal:", self.__genero



class Perro(Animal):
    def __init__(self, edad: str, nombreDueño: str, nombreAnimal: str, genero: str, razaP: str):
        super().__init__(edad, nombreDueño, nombreAnimal, genero)
        self.__razaP = razaP

    def getRaza(self) -> str:
        print("Raza Perro:", self.__razaP)

    def setRaza(self, raza: str) -> None:
        self.__razaP = raza



class Gato(Animal):
    def __init__(self, edad: str, nombreDueño: str, nombreAnimal: str, genero: str, razaG: str):
        super().__init__(edad, nombreDueño, nombreAnimal, genero)

        self.__razaG = razaG

    def getRaza(self) -> str:
        print("Raza Gato:", self.__razaG)

    def setRaza(self, raza: str) -> None:
        self.__razaG = raza


class Ave(Animal):
    def __init__(self, edad: str, nombreDueño: str, nombreAnimal: str, genero: str, tipo: str):
        super().__init__(edad, nombreDueño, nombreAnimal, genero)
        self.__tipo = tipo

    def getRaza(self) -> str:  
        print("Tipo de Ave:", self.__tipo)

    def setRaza(self, tipo: str) -> None:
        self.__tipo = tipo


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