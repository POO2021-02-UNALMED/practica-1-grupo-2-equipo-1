from noPersonas.bebida import Bebida

class Cafe(Bebida):
    _inventarioCafe = 9
    _codigoCafe = 1000
    _PRECIOCAFE = 5000
    
    def __init__(self):
        super().__init__(Cafe._codigoCafe, Cafe._PRECIOCAFE)
        self._codigo = Cafe._codigoCafe
        self._codigo += 1
        self._precio = Cafe._PRECIOCAFE
        Cafe._inventarioCafe += 1
    
    @classmethod
    def getInventarioCafe(cls):
        return cls._inventarioCafe
    
    @classmethod
    def setInventarioCafe(cls, inventarioCafe):
        cls._inventarioCafe = inventarioCafe
    
    def __str__(self):
        activo = '\nCafe'
        formatoFactura = ('%-25s')%activo
        formatoFactura = formatoFactura.replace(' ', '.')
        formatoFactura += str(self._precio)
        return formatoFactura    

    @staticmethod
    def prepararCafes(i):
        while i > 0:
            Cafe()
            i += -1
    