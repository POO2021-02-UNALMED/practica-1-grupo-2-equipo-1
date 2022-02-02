from errorAplicacion import ErrorAplicacion

class ExcepcionSinInfo(ErrorAplicacion):
    def __init__(self, mensaje):
        super().__init__("No se encuentra información para avalar " + mensaje)