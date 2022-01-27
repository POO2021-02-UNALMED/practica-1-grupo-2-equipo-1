from empleado import Empleado
from noPersonas.orden import Orden

class Barista(Empleado):
    _baristas = []
    _SUELDO = 908526
    
    def __init__(self, cedula, nombre):
        super().__init__(cedula, nombre, Barista._SUELDO)
        self._cedula = cedula
        self._nombre = nombre
        Barista._baristas.append(self)
    
    def __str__(self):
        return 'El barista ' + self._nombre + ' identificado con el número de cedula ' + self._cedula + ' tiene como funciones: atender al cliente, vigilar el local y recibir ordenes por parte de su administrador'
    
    @classmethod
    def getBaristas(cls):
        return cls._baristas
    
    @classmethod
    def getSueldo(cls):
        return cls._SUELDO
    
    @classmethod
    def setBaristas(cls, baristas):
        cls._baristas = baristas
    
    def getOrdenes(self):
        return self._ventas

    def getComisionVentas(self):
        return self._comisionVentas
    
    def setOrdenes(self, ordenes):
        self._ordenes = ordenes
    
    def getNombre(self):
        return self._nombre
    
    def setComisionVentas(self, comisionVentas):
        self._comisionVentas = comisionVentas
    
    def getVentas(self):
        return self._ventas
    
    def getVentasAcumuladoas(self):
        return self._ventasAcumuladas
    
    def getComisionAcumulada(self):
        return self._comisionAcumulada
    
    def setVentas(self, ventas):
        self._ventas = ventas

    def setVentasAcumuladas(self, ventasAcumuladas):
        self._ventasAcumuladas = ventasAcumuladas;

    def setComisionAcumulada(self, comisionAcumulada):
        self._comisionAcumulada = comisionAcumulada