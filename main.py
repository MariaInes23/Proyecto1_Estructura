from Vehiculo import ClaseVehiculo
from Mantenimiento import ClaseMantenimiento
from FlotaVehiculos import ClaseFlotaVehiculos

flota = ClaseFlotaVehiculos()


def menu():

    while True:
        print()
        print("+------------------------------+")
        print("|         MENÚ - TALLER        |")
        print("+------------------------------+")
        print("| 1. Registrar Vehículo        |")
        print("| 2. Eliminar Vehículo         |")
        print("| 3. Buscar Vehículo           |")
        print("| 4. Listar Vehículos          |")
        print("| 5. Realizar Mantenimiento    |")
        print("| 6. Salir                     |")
        print("+------------------------------+")
        print()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
             print()
             print("+------------------------------+")
             print("|            AGREGAR           |")
             print("+------------------------------+")
             try:
                placa = input("Ingrese la placa del vehículo (7 caracteres con Numeros y Letras): ")
                vehiculo = ClaseVehiculo(placa, "", "", "", "")
                vehiculo.placa = placa 
                
                año = input("Ingrese el año del vehículo: ")
                vehiculo.año = año
                
                kilometraje = input("Ingrese el kilometraje del vehículo: ")
                vehiculo.kilometraje = kilometraje
                
                marca = input("Ingrese la marca del vehículo: ")
                modelo = input("Ingrese el modelo del vehículo: ")
                
                vehiculo = ClaseVehiculo(placa, marca, modelo, año, kilometraje)
                flota.registrar_vehiculo(vehiculo)
                print("Vehículo registrado correctamente.")
            
             except ValueError as e:
                print(f"Error: {e}")

            
        elif opcion == "2":
             print()
             print("+------------------------------+")
             print("|           ELIMINAR           |")
             print("+------------------------------+")
             placa = input("Ingrese la placa del vehículo a eliminar: ")
             flota.eliminar_vehiculo(placa)    

        elif opcion == "3":
             print()
             print("+------------------------------+")
             print("|            BUSCAR            |")
             print("+------------------------------+")
             placa = input("Ingrese la placa del vehículo a buscar: ")
             vehiculo = flota.buscar_vehiculo(placa)
             if vehiculo:
                print(f'Vehículo encontrado: Placa: {vehiculo.placa}, Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Año: {vehiculo.año}, Kilometraje: {vehiculo.kilometraje}')
                print()
                print("-------Historial de Mantenimientos-------")
                vehiculo.mostrar_historial()
                print("-------Costo Total-------")
                vehiculo.calcular_costo_total_mantenimientos()
             else:
                print("No se encontró el vehículo.")
           
        elif opcion == "4":
             print()
             print("+------------------------------+")
             print("|           LISTAR             |")
             print("+------------------------------+")
             flota.listar_vehiculos()
        
        elif opcion == "5":
            print()
            print("+------------------------------+")
            print("|    REALIZAR MANTENIMIENTO    |")
            print("+------------------------------+")
            placa = input("Ingrese la placa del vehículo para agregar mantenimiento: ")
            vehiculo = flota.buscar_vehiculo(placa)
            if vehiculo:
                 fecha = input("Ingrese la fecha del mantenimiento: ")
                 descripcion = input("Ingrese la descripción: ")
                 costo = float(input("Ingrese el costo del mantenimiento: "))
                 mantenimiento = ClaseMantenimiento(fecha, descripcion, costo)
                 if isinstance(vehiculo, ClaseVehiculo):
                    vehiculo.agregar_mantenimiento(mantenimiento)
                 else:
                    print("ERROR")
                 print("Mantenimiento agregado correctamente.")


        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

menu()