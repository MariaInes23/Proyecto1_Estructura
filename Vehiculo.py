class ClaseVehiculo:
    def __init__(self, placa, marca, modelo, año, kilometraje, historial):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje
        self.historial = historial
        
    @property
    def placa(self):
        return self._placa
    

    @placa.setter
    def placa(self, nueva_placa): 
        if len(nueva_placa) == 6 and nueva_placa.isalnum(): #Validación: 6 caracteres alfanumericos
            self._placa = nueva_placa
        else:
            raise ValueError("La placa debe tener 6 caracteres y ser alfanumérica.")