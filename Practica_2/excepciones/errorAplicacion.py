import imp
import tkinter as tk
class ErrorAplicacion(Exception):
    def __init__(self, mensaje):
        super().__init__("Se encontró un error")
        self._mensaje = mensaje

    def mostrarMensaje(self):
        tk.messagebox.showwarning('Error', "Manejo de errores de la Aplicación: " + self._mensaje)
