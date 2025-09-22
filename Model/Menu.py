

from Entities.animal import Animal
from Entities.Citas import Citas
from Entities.genero import Genero
from Entities.Raza_animal import Raza_animal
from Entities.Servicios import Servicios
from Entities.Tipo_animal import Tipo_animal
from Entities.usuario import Usuario
from sqlalchemy.orm import Session


class MiServicio:
    def __init__(self, db: Session):
        self.db = db
        self.animal = Animal(self.db)
        self.citas = Citas(self.db)
        self.genero = Genero(self.db)
        self.raza_animal = Raza_animal(self.db)
        self.servicios = Servicios(self.db)
        self.tipo_animal = Tipo_animal(self.db)
        self.usuario = Usuario(self.db)

    def Ejecucion(self):
        print("prueba")

    """def menu():
        mj = 1
        fac = Fac.Factura(mj)
        sev = Sev.Servicios(fac)
        
        while True:
            print("--Veterinaria EL Zancudo--")
            print("--------------------------")
            print("MENU DE APLICACION")
            print("1. manejo animales")
            print("2. manejo cita")
            print("3. pagar facturas")
            print("0. Salir programa")
            print("ingrese una opcion")
            opcion=int(input())
            
            match opcion:
                case 1:
                    print("---sub-menu animales---") 
                    print("1. Crear ") 
                    print("2. Eliminar ") 
                    print("3. Buscar ")
                    print("0. Salir sub-menu ")
                    opcion1=int(input())
                    match opcion1:
                        case 1:
                            edad=int(input("Ingrese la edad: "))
                            NomAnimal=input("Ingrese el nombre: ")
                            NomDueño=input("Ingrese el nombre dueño: ")
                            genero=input("Ingrese el genero del animal: ")
                            Tipo=input("Ingrese el tipo de la mascota: \n P-perro G-gato  A-ave\n:")
                            animal=None
                            match Tipo:
                                case 'P':
                                    razap=input("Raza del perro: ")
                                    animal= Perro(edad,NomDueño,NomAnimal,genero,razap)
                                case 'G':
                                    razag=input("Raza del garto: ")
                                    animal= Gato(edad,NomDueño,NomAnimal,genero,razag)
                                case 'A':
                                    tipoA=input("Tipo del ave: ")
                                    animal= Ave(edad,NomDueño,NomAnimal,genero,tipoA)
                                case _:
                                    print("error de ingreso")
                            if animal!= None:
                                mj.CrearAnimal(animal)

                        case 2:
                            print("Eliminar Animal")
                            nombreA=input("ingrese el nombre del Animal: ")
                            mj.BorrarAnimal(nombreA)
                        case 3:
                            print("Buscador de animales")
                            nombreA=input("ingrese el nombre del Animal: ")
                            mj.BuscarAnimal(nombreA)
                        case 0:
                            print("saliendo del programa")
                        case _:
                            print("opcion no valida")     
                case 2:
                    print("---sub menu citas---")
                    print("1. Agendar cita")
                    print("2. Atender cita")
                    print("0. Salir menu pricipal")
                    print("Ingrese una opcion")

                    opcion1=int(input())
                    match opcion1:
                        case 1:
                            NomAnimal=input("Ingrese el nombre del animal: ")
                            obj=mj.BuscarAnimal(NomAnimal)
                            if obj==None:
                                print("Para asignar cita a un animal debe estar crearlo")
                                break
                            else:
                                sev.AgendarCita(obj)
                        case 2:
                            sev.AtenderCita()
                        case 0:
                            print("Saliendo..")
                        case _:
                            print("opcion no valida")  
                case 3:
                    print("pasarela de pago....")
                    NomAnimal=input("Ingrese el nombre del animal que tiene la factura: ")
                    fac.facturar(NomAnimal)

                case 0:
                    print("saliendo del progama")
                    break
                case _:
                    print("VALOR INGRESADO NO DISPONIBLE")"""

def main(): 
    mi_servicio = MiServicio(db=None)
    mi_servicio.Ejecucion() 

               
                
if __name__ == '__main__':
    main()