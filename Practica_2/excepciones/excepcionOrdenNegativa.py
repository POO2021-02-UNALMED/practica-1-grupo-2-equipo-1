from excepcionNegativos import ExcepcionNegativos

class ExcepcionOrdenNegativa(ExcepcionNegativos):
    def __init__(self, negativo):
        super().__init__("realizar un pedido, ingrese la orden correcta", negativo)