from orden import Orden

class OrdenPresencial(Orden): 
    _numeroOrdenes = 1000;
    _ordenesCreadas = 0
    
    def __init__(self, bebidas, cliente, barista):
        self._numeroOrden = OrdenPresencial._ordenesCreadas
        OrdenPresencial._ordenesCreadas += 1
        self._numeroOrden = OrdenPresencial._numeroOrdenes
        OrdenPresencial._numeroOrdenes += 1
        self._bebidas = bebidas
        self._cliente = cliente
        self._barista = barista
        acumulado = 0;
		
        for x in self.bebidas:
            acumulado += x.getPrecio()
            
        #self._costo = acumulado
    
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

	'''public void aplicarPromocion(Promocion promocion) {
		if(promocion.equals(Promocion.CAFE2X1) && ActivarPromocion.isPromos()) {
			this.costo -= 5000;
		} else if(promocion.equals(Promocion.JUGO2X1) && ActivarPromocion.isPromos()) {
			this.costo -= 4000;
		} else if (promocion.equals(Promocion.CAFECONJUGOAL50) && ActivarPromocion.isPromos()){
			this.costo -= 4500;
		}
	}'''
    
    def __str__(self):
        return self.barista.getNombre() + " le vendió a " + self.cliente.getNombre()+" la orden número " + self.numeroOrden + " por un valor de " + self.costo

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