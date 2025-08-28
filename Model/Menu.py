def main():


    while True:
        print("--Veterinaria EL Zancudo--")
        print("--------------------------")
        print("MENU DE APLICACION")
        print("1. manejo animales")
        print("2. Crear cita")
        print("3. pagar facturas")
        
        opcion=input("Ingrese una opcion")
        
        match opcion:
            case "1":
                print("---sub menu---") 