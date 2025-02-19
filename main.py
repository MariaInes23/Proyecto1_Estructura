from Vehiculo import ClaseVehiculo
from Mantenimiento import ClaseMantenimiento
from FlotaVehiculos import ClaseFlotaVehiculos

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
             placa = input("Ingrese la placa del vehículo (6 caracteres alfanuméricos): ")
             try:
                    marca = input("Ingrese la marca del vehículo: ")
                    modelo = input("Ingrese el modelo del vehículo: ")
                    año = input("Ingrese el año del vehículo: ")
                    kilometraje = input("Ingrese el kilometraje del vehículo: ")
                    historial = []  # Inicializarlo vacío o con datos si es necesario

                    # Crear el objeto vehiculo con todos los datos
                    vehiculo = ClaseVehiculo(placa, marca, modelo, año, kilometraje, historial)
                    
                    # Verificar que las variables tienen datos
                    print(f"Placa: {placa}, Marca: {marca}, Modelo: {modelo}, Año: {año}, Kilometraje: {kilometraje}, Historial: {historial}")
                    print("Vehículo registrado correctamente.")
             except ValueError as e:
                    print(f"Error: {e}")
        
        elif opcion == "2":
            print("\n BUSCAR")      
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