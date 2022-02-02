from excepcionNegativos import ExcepcionNegativos

class ExcepcionPreparacionNegativa(ExcepcionNegativos):
    def __init__(self, negativo):
        super().__init__("la preparación de bebidas, ingrese el número correcto de bebidas a preparar", negativo)