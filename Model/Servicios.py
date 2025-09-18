from queue import  Queue
import factura as fac
import Manejo_animales as MjA 

class Servicios:
    
    def __init__(self, factura):
        self.ServiciosT = [("Vacunar", 50000),
                           ("Limpieza", 150000)]
        self.ColaCitas = Queue()
        self.factura = factura 

    def AgendarCita(self, animal)->None:
        print("Que Servicio se va realizar durante la cita:\n1:Vacunar costo-$50000 | 2:Limpiesa costo-$150000")
        Opserv=int(input())
        if Opserv==1:
            Servicio, valor = self.ServiciosT[0]
        elif Opserv==2:
            Servicio, valor = self.ServiciosT[1]
        else:
            print("Opcion no valida")
            return
        self.ColaCitas.put((animal, Servicio))
        
        # Subfacturar
        self.factura.subFacturar(animal. getnombreAnimal(), Servicio, valor)
        print("Cita Agendada correctamente")
    
    def AtenderCita(self)->None:
        if self.ColaCitas.empty():
            print("No hay citas pendientes.")
            return
        print("Atendiendo cita....")
        cita=self.ColaCitas.get()
        animal = cita[0] 
        Servicio=cita[1] 
        print(f"El animal {animal.getnombreAnimal()} se realiazo el servicio de {Servicio}")
        
    

