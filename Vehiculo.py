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
        
        
    @property
    def año(self):
        return self._año
    
    @año.setter
    def año(self, dato1): 
        dato1 = int(dato1)
        if dato1 > 1900 and dato1 < 2025:
            self._año = dato1
        else:
            raise ValueError("Año invalido")
        

    @property
    def kilometraje(self):
        return self._kilometraje
    
    @kilometraje.setter
    def kilometraje(self, dato): 
        dato = int(dato)
        if dato > 0:
            self._kilometraje = dato
        else:
            raise ValueError("Kilometraje invalido")