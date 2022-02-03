from excepciones.excepcionNegativos import ExcepcionNegativos

class ExcepcionFueraDeRango(ExcepcionNegativos):
    def __init__(self, numero):
        super().__init__("orden", numero)