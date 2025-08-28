class Animal():
    def __init__(self, edad:str, nombreDueño: str, nombreAnimal: str, genero: str):
        self.edad = edad
        self.nombreDueño = nombreDueño
        self.genero = genero
        self.nombreAnimal = nombreAnimal
        
    def getnombreAnimal(self):
        print("Nombre Animal:", self.nombreAnimal)
        
    def getnombreDueño(self):
        print("Nombre Dueño:", self.nombreDueño)
        
    def getedadAnimal(self):
        print("Edad:", self.edad)
        
    def getgeneroAnimal(self):
        print("Nombre Animal:", self.genero)