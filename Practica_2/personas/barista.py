from empleado import Empleado
from noPersonas.orden import Orden
from noPersonas.ordenVirtual import OrdenVirtual

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
    
    def prepararVenta(self, bebidas, cliente, domiciliario = '', promocion = ''):
        orden = OrdenVirtual(bebidas, cliente, self, domiciliario)
        orden.aplicarPromocion(promocion)
        
        if domiciliario != '':
            retorno = '\nOrden '+orden.getNroOrden()+'\n\npreparada por\n'+ self._nombre +'\n\nse le entrega a\n'+ domiciliario.getNombre() + '\n\npara ser entregada a \n' + cliente.getNombre()+'\n'
        else:
            retorno = '\nOrden '+orden.getNroOrden()+'\n\npreparada por\n'+ self._nombre+ '\n\npara ser entregada a \n' + cliente.getNombre()+'\n'
        
        for x in bebidas:
            retorno += x.__str__()
        
        if promocion != '':
            valorFactura =('%-23s')%'Valor_con_promo'
        else:
            valorFactura =('%-23s')%'Valor_total'
        valorFactura = valorFactura.replace(' ', '.')
        retorno += "\n" + valorFactura + orden.getCosto()
        self._ventas.append(orden)
        self._ventasAcumuladas += orden.getCosto()
        self.comisionVentas += (orden.getCosto() * self._comisionAcumulada)/100;
		
        if self._ventasAcumuladas >= 20000:
            if self._ventasAcumuladas >= 50000:
                self._comisionAcumulada = 5
            else:
                self._comisionAcumulada = 2
    
        return retorno;
        