from excepcionSinInfo import ExcepcionSinInfo

class ExcepcionSobreInventario(ExcepcionSinInfo):
    def __init__(self):
        super().__init__("el inventario necesario para cumplir esta venta, registre la preparación de más bebidas")