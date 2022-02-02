from Practica_2.excepciones.excepcionSinInfo import ExcepcionSinInfo

class ExcepcionInicioSesion(ExcepcionSinInfo):
    def __init__(self):
        super().__init__("el inicio de sesión, vuelva a intentarlo con credenciales válidas")

