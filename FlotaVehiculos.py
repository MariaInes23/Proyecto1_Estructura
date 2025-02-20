from Vehiculo import ClaseVehiculo

class NodoVehiculo:
    def __init__(self, vehiculo=None):
        self.vehiculo = vehiculo
        self.siguiente = None
        self.anterior = None

class ClaseFlotaVehiculos:
    def __init__(self):
        self.cabeza = None

    def registrar_vehiculo(self, vehiculo):
        nuevo_nodo = NodoVehiculo(vehiculo)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual

    def eliminar_vehiculo(self, placa):
        actual = self.cabeza
        while actual:
            if actual.vehiculo.placa == placa:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                if actual == self.cabeza:
                    self.cabeza = actual.siguiente
                del actual
                print(f'Vehículo con placa {placa} eliminado.')
                return
            actual = actual.siguiente
        print(f'Vehículo con placa {placa} no encontrado.')

    def listar_vehiculos(self):
        actual = self.cabeza
        while actual:
            v = actual.vehiculo
            print(f'Placa: {v.placa}, Marca: {v._marca}, Modelo: {v._modelo}, Año: {v.año}, Kilometraje: {v.kilometraje}')
            actual = actual.siguiente

    def buscar_vehiculo1(self, placa):
        actual = self.cabeza
        while actual:
            if actual.vehiculo.placa == placa:
                v = actual.vehiculo
                print(f'Placa: {v.placa}, Marca: {v._marca}, Modelo: {v._modelo}, Año: {v.año}, Kilometraje: {v.kilometraje}')
                return
            actual = actual.siguiente
        print(f'Vehículo con placa {placa} no encontrado.')
    
    def buscar_vehiculo(self, placa):
        actual = self.cabeza
        while actual:
            if actual.vehiculo.placa == placa:
                if isinstance(actual.vehiculo, ClaseVehiculo):
                    return actual.vehiculo
                else:
                    print("El objeto encontrado no es una instancia válida de Vehiculo.")
                    return None
            actual = actual.siguiente
        print(f'Vehículo con placa {placa} no encontrado.')
        return None
    