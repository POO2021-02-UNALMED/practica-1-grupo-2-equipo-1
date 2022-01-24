from bebida import Bebida

class Cafe(Bebida):
    _inventarioCafe = 0
    _PRECIOCAFE = 5000
    
    def __init__(self, codigoCafe):
        self._codigoCafe = codigoCafe
        Cafe._inventarioCafe += 1
    
    @classmethod
    def getInventarioCafe(cls):
        return cls._inventarioCafe
    
    @classmethod
    def setInventarioCafe(cls, inventarioCafe):
        cls._inventarioCafe = inventarioCafe
    
    def __str__(self):
        activo = '\nCafe'
        formatoFactura = '' #??
        formatoFactura += self._precio
        return formatoFactura    

    @staticmethod
    def prepararCafes(cls, i):
        while i > 0:
            Cafe()
            i -= 1
    