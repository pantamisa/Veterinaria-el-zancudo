from Manejo_animales import ManejoAnimales

class Factura:
    def __init__(self, manejador_animales : ManejoAnimales):
        self.facturacion = {}  # Diccionario para almacenar servicios y costos por animal
        self.manejador = manejador_animales  #de manejo animales

    def subFacturar(self, nombreAnimal: str, servicio: str, costo: float) -> None:
        animal = self.manejador.BuscarAnimal(nombreAnimal)
        if not animal:
            print(f"El animal '{nombreAnimal}' no está registrado en el sistema.")

            return
        
        if nombreAnimal not in self.facturacion:
            self.facturacion[nombreAnimal] = []
        self.facturacion[nombreAnimal].append((servicio, costo))
        print(f"Servicio '{servicio}' agregado a {nombreAnimal} (${costo})")

    def facturar(self, nombreAnimal: str) -> float:
        animal = self.manejador.BuscarAnimal(nombreAnimal)
        if not animal:
            print("No se puede facturar. El animal " + nombreAnimal+ "no existe en el sistema.")
            return 0.0
        
        if nombreAnimal not in self.facturacion:
            print("⚠ No hay servicios registrados para " + nombreAnimal)
            return 0.0
        
        total = sum(costo for _, costo in self.facturacion[nombreAnimal])

        print("\n📄 Factura de " + nombreAnimal + ":")
        for servicio, costo in self.facturacion[nombreAnimal]:
            print(f"- {servicio}: ${costo}")   
        print(f"➡ Total: ${total}\n")         
        return total
