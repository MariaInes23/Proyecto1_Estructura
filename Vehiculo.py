class NodoMantenimiento:
    def __init__(self, mantenimiento=None):
        self.mantenimiento = mantenimiento
        self.siguiente = None

class ListaEnlazadaMantenimientos:
    def __init__(self):
        self.cabeza = None

    def agregar(self, mantenimiento):
        nuevo_nodo = NodoMantenimiento(mantenimiento)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        if not actual:
            print('No hay mantenimientos realizados')
            return
        while actual:
            print(f'{actual.mantenimiento.fecha}: {actual.mantenimiento.descripcion} - Q{actual.mantenimiento.costo}')
            actual = actual.siguiente

class ClaseVehiculo:
    def __init__(self, placa, marca, modelo, año, kilometraje, historial= None):
        self._placa = placa
        self._marca = marca
        self._modelo = modelo
        self._año = año
        self._kilometraje = kilometraje
        self._mantenimientos = historial if historial else ListaEnlazadaMantenimientos()

    @property
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return self._modelo
        
    @property
    def placa(self):
        return self._placa
    

    @placa.setter
    def placa(self, nueva_placa): 
        if len(nueva_placa) == 7 and nueva_placa.isalnum(): 
            self._placa = nueva_placa
        else:
            raise ValueError("La placa debe tener 7 caracteres, entre numeros y letras")
        
        
    @property
    def año(self):
        return self._año
    
    @año.setter
    def año(self, dato1): 
        dato1 = int(dato1)
        if dato1 > 1900 and dato1 < 2026:
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
        

    def agregar_mantenimiento(self, mantenimiento):
        self._mantenimientos.agregar(mantenimiento)

    def mostrar_historial(self):
        self._mantenimientos.mostrar()

        