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
        print("5. Realizar Mentenimiento")
        print("6. Salir")
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
             vehiculo = flota.buscar_vehiculo(placa)
             if vehiculo:
                print(f'Vehículo encontrado: Placa: {vehiculo.placa}, Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Año: {vehiculo.año}, Kilometraje: {vehiculo.kilometraje}')
                print("Historial de Mantenimientos:")
                vehiculo.mostrar_historial()
             else:
                print("No se encontró el vehículo.")
           
        elif opcion == "4":
            print("\n LISTAR")
            flota.listar_vehiculos()
        
        elif opcion == "5":
            print("\n REALIZAR MANTENIMIENTO")
            placa = input("Ingrese la placa del vehículo para agregar mantenimiento: ")
            vehiculo = flota.buscar_vehiculo(placa)
            if vehiculo:
                 fecha = input("Ingrese la fecha del mantenimiento: ")
                 descripcion = input("Ingrese la descripción del servicio: ")
                 costo = float(input("Ingrese el costo del mantenimiento: "))
                 mantenimiento = ClaseMantenimiento(fecha, descripcion, costo)
                 if isinstance(vehiculo, ClaseVehiculo):
                    vehiculo.agregar_mantenimiento(mantenimiento)
                 else:
                    print("El vehículo no es una instancia válida de la clase Vehiculo.")
                 print("Mantenimiento agregado correctamente.")


        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

menu()