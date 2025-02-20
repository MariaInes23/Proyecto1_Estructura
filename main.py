from Vehiculo import ClaseVehiculo
from Mantenimiento import ClaseMantenimiento
from FlotaVehiculos import ClaseFlotaVehiculos

flota = ClaseFlotaVehiculos()

def menu():

    while True:
        print("\nMENÚ")
        print("1. Registrar Vehículo")
        print("2. Eliminar Vehículo")
        print("3. Buscar Vehículo")
        print("4. Listar Vehículos")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
             placa = input("Ingrese la placa del vehículo: ")
             marca = input("Ingrese la marca: ")
             modelo = input("Ingrese el modelo: ")
             año = int(input("Ingrese el año: "))
             kilometraje = float(input("Ingrese el kilometraje: "))
             vehiculo = ClaseVehiculo(placa, marca, modelo, año, kilometraje)
             flota.registrar_vehiculo(vehiculo)
             print("Vehículo registrado correctamente.")
        
        elif opcion == "2":
            print("\n ELIMINARR")  
            placa = input("Ingrese la placa del vehículo a eliminar: ")
            flota.eliminar_vehiculo(placa)    
        elif opcion == "3":
            print("\n BUSCAR")
            placa = input("Ingrese la placa del vehículo a buscar: ")
            flota.buscar_vehiculo(placa)
           
        elif opcion == "4":
            print("\n LISTAR")
            flota.listar_vehiculos()

        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

menu()