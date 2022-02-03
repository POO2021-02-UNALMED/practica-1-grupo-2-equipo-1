from noPersonas.orden import Orden
from personas.barista import Barista
#from personas.cliente import Cliente
from noPersonas.promocion import Promocion

class OrdenPresencial(Orden): 
    _numeroOrdenes = 1000;
    _ordenesCreadas = 0
    
    def __init__(self, bebidas, cliente, barista):
        OrdenPresencial._ordenesCreadas += 1
        self._numeroOrden = OrdenPresencial._numeroOrdenes
        OrdenPresencial._numeroOrdenes += 1
        self._bebidas = bebidas
        self._cliente = cliente
        self._barista = barista
        acumulado = 0;
        barista._ventas.append(self)
		
        for x in self._bebidas:
            acumulado += x.getPrecio()
            
        self._costo = acumulado
    
    def getBebidas(self):
        return self._bebidas;
    
    @classmethod
    def getOrdenesCreadas(cls):
        return cls._ordenesCreadas
    
    def setBebidas(self, bebidas):
        self._bebidas = bebidas

    @classmethod
    def setOrdenesCreadas(cls, ordenesCreadas):
        cls._ordenesCreadas = ordenesCreadas

    def aplicarPromocion(self, promocion):
        if promocion == Promocion.CAFE2X1: # && ActivarPromocion.isPromos():
            self._costo -= 5000
        elif promocion == Promocion.JUGO2X1: # && ActivarPromocion.isPromos():
            self._costo -= 4000
        elif promocion == Promocion.CAFECONJUGOAL50: # && ActivarPromocion.isPromos()):
            self._costo -= 4500
    
    def __str__(self):
        return self._barista.getNombre() + ' le vendió a ' + self._cliente.getNombre()+' la orden número ' + str(self._numeroOrden) + ' por un valor de ' + str(self._costo)

    @classmethod
    def getNumeroOrdenes(cls):
        return cls._numeroOrdenes
    
    def getProductos(self):
        return self._bebidas
    
    def getCliente(self):
        return self._cliente
    
    def getBarista(self):
        self._barista
    
    def getNumeroOrden(self):
        return self._numeroOrden
    
    def getCosto(self):
        return self._costo

    @classmethod
    def setNumeroOrdenes(cls, numeroOrdenes):
        cls._numeroOrdenes = numeroOrdenes;
    
    def setProductos(self, bebidas):
        self._bebidas = bebidas
    
    def setCliente(self, cliente):
        self._cliente = cliente

    def setBarista(self, barista):
        self._barista = barista

    def setNumeroOrden(self, numeroOrden):
        self.numeroOrden = numeroOrden
    
    def setCosto(self, costo):
        self._costo = costo