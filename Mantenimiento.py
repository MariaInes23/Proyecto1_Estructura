class ClaseMantenimiento:
    def __init__(self, fecha, descripcion, costo):
        self.fecha = fecha
        self.descripcion = descripcion
        self.costo = costo


    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, valor):
        if isinstance(valor, str):
            self._fecha = valor
        else:
            raise ValueError('La fecha es invalida')
        
    
    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, valor):
        if isinstance(valor, str):
            self._descripcion = valor
        else:
            raise ValueError('La descripción debe ser una cadena de texto.')

    @property
    def costo(self):
        return self._costo

    @costo.setter
    def costo(self, valor):
        if isinstance(valor, (int, float)) and valor > 0:
            self._costo = valor
        else:
            raise ValueError('El costo debe ser un número positivo.')