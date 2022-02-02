from errorAplicacion import ErrorAplicacion

class ExcepcionNegativos(ErrorAplicacion):
    def __init__(self, mensaje, negativo):
        super().__init__(str(negativo) + "no es un número válido para " + mensaje)