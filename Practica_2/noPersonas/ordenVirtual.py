from noPersonas.orden import Orden
from noPersonas.promocion import Promocion

class OrdenVirtual(Orden):
    _ordenesVirtuales = []
    _nroOrdenes = 2000
    _ordenesCreadas = 0

    def __init__(self, bebidas, cliente, barista, domiciliario):
        OrdenVirtual._ordenesCreadas += 1
        self._nroOrden = OrdenVirtual._nroOrdenes
        OrdenVirtual._nroOrdenes += 1
        self._bebidas = bebidas
        self._cliente = cliente
        self._barista = barista
        self._domiciliario = domiciliario
        acumulado = 0
        OrdenVirtual._ordenesVirtuales.append(self)
        
        for x in self._bebidas:
            acumulado += x.getPrecio()
        
        self._costo = acumulado
        OrdenVirtual._ordenesVirtuales.append(self)
    
    @classmethod
    def getOrdenesCreadas(cls):
        return cls._ordenesCreadas
    
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
    
    def reportarIncidente(self):
        self._domiciliario.setIncidentes(True)
    
    def __str__(self):
        return self._barista.getNombre() + ' le vendió a ' + self._cliente.getNombre()+' la orden número ' + self._nroOrden + ' por un valor de ' + self._costo
    
    @classmethod
    def getOrdenesVirtuales(cls):
        return cls._ordenesVirtuales
    
    @classmethod
    def setOrdenesVirtuales(cls, ordenesVirtuales):
        cls._ordenesVirtuales = ordenesVirtuales
    
    @classmethod
    def getNroOrdenes(cls):
        return cls._nroOrdenes
    
    def getBebidas(self):
        return self._bebidas
    
    def getCliente(self):
        return self._cliente;
    
    def getBarista(self):
        return self._barista
    
    def getDomiciliario(self):
        return self._domiciliario

    def getNroOrden(self):
        return self._nroOrden

    def getCosto(self):
        return self._costo

    @classmethod
    def setNroOrdenes(cls,nroOrdenes):
        cls._nroOrdenes = nroOrdenes
    
    def setBebidas(self, bebidas):
        self._bebidas = bebidas

    def setCliente(self, cliente):
        self._cliente = cliente

    def setBarista(self, barista):
        self._barista = barista

    def setDomiciliario(self, domiciliario):
        self._domiciliario = domiciliario

    def setNroOrden(self, nroOrden):
        self._nroOrden = nroOrden

    def setCosto(self, costo):
        self._costo = costo