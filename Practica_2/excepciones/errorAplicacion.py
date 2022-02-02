class ErrorAplicacion(Exception):
    def __init__(self, mensaje):
        super().__init__("Se encontró un error")
        self._mensaje = mensaje

    def mostrarMensaje(self):
        print("Manejo de errores de la Aplicación: " + self._mensaje)
