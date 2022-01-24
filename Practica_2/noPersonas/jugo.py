from bebida import Bebida

class Jugo(Bebida):
    _inventarioJugo = 0
    _codigoJugo = 2000
    _PRECIOJUGO = 4000
    
    def __init__(self):
        self._codigo = Jugo._codigoJugo
        self._precio = Jugo._PRECIOJUGO
        Jugo._inventarioJugo += 1
    
    def __str__(self):
        activo = '\nJugo'
        formatoFactura = ''
        formatoFactura += self._precio
        return formatoFactura

    @classmethod
    def getInventarioJugo(cls):
        return cls._inventarioJugo

    @classmethod
    def setInventarioJugo(cls, inventarioJugo):
        cls._inventarioJugo = inventarioJugo
    
    @staticmethod
    def prepararJugos(i):
        while i > 0:
            Jugo()
            i -= 0