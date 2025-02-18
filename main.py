from Vehiculo import Vehiculo
from Mantenimiento import Mantenimiento
from FlotaVehiculos import FlotaVehiculos

def menu():
    #vehiculo = Vehiculo()
    #mantenimiento = Mantenimiento()
    flota = FlotaVehiculos()

    while True:
        print("\nMENÚ")
        print("1. Registrar Vehículo")
        print("2. Eliminar Vehículo")
        print("3. Buscar Vehículo")
        print("4. Listar Vehículos")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            print("\nREGISTRAR VEHÍCULO")
            placa = input("Ingrese placa: ")
            marca = input("Ingrese marca: ")
            modelo = input("Ingrese modelo: ")
            año = input("Ingrese el año: ")
            kilometraje = input("Ingrese el kilometraje: ")
            historial = input("Ingrese el historial: ")
            flota.ingresarVehiculo(placa, marca, modelo, año, kilometraje, historial)
            
        elif opcion == "2":
            print("\n ELIMINAR")
        
        elif opcion == "3":
            print("\n BUSCAR")
           
        elif opcion == "4":
            print("\n LISTAR")

        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
menu()