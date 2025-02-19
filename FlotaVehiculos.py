from Vehiculo import ClaseVehiculo

class ClaseFlotaVehiculos:
    def __init__(self):
        self.cabeza = None
    
    def ingresarVehiculo(self, placa, marca, modelo, año, kilometraje, historial):
        nuevoVehiculo = ClaseVehiculo(placa, marca, modelo, año, kilometraje, historial)
    
        actual = self.cabeza
        while actual.siguiente and actual.siguiente:
            actual = actual.siguiente
        
        nuevoVehiculo.siguiente = actual.siguiente
        actual.siguiente = nuevoVehiculo
    