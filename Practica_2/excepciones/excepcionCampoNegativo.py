from excepciones.excepcionNegativos import ExcepcionNegativos

class ExcepcionCampoNegativo(ExcepcionNegativos):
    def __init__(self, negativo):
        super().__init__("llenar un campo", negativo)