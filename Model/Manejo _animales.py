class ManejoAnimales:
    def __init__(self):
        # Arreglo para almacenar los animales
        self.animales = []

    def CrearAnimal(self, animal):
        """Agrega un animal a la lista"""
        self.animales.append(animal)
        print(f"Animal {animal.Getnombre()} agregado con éxito.")

    def BorrarAnimal(self, nombre):
        """Elimina un animal por su nombre"""
        for a in self.animales:
            if a.Getnombre() == nombre:
                self.animales.remove(a)
                print(f"Animal {nombre} eliminado con éxito.")
                return True
        print(f"No se encontró el animal {nombre}.")
        return False

    def BuscarAnimal(self, nombre):
        """Busca un animal por su nombre y lo retorna"""
        for a in self.animales:
            if a.Getnombre() == nombre:
                return a
        return None

    def AñadirVacuna(self, nombre, vacuna):
        """Añade una vacuna al animal especificado"""
        animal = self.BuscarAnimal(nombre)
        if animal:
            if not hasattr(animal, "vacunas"):
                animal.vacunas = []
            animal.vacunas.append(vacuna)
            print(f"Vacuna '{vacuna}' añadida a {nombre}.")
            return True
        else:
            print(f"No se encontró el animal {nombre}.")
            return False
