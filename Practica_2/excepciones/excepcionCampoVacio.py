from excepciones.excepcionSinInfo import ExcepcionSinInfo

class ExcepcionCampoVacio(ExcepcionSinInfo):
    def __init__(self, criterio):
        super().__init__("necesita llenar " + criterio)