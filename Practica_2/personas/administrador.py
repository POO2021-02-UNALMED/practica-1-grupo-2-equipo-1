from empleado import Empleado

class Administrador(Empleado):
    def __init__(self, cedula, nombre, sueldo, usuario, contrasena):
        self._cedula = cedula
        self._nombre = nombre
        self._sueldo = sueldo
        self._usuario = usuario
        self._contrasena = contrasena
        
    def __str__(self):
        return  "El administrador " + self._nombre + " identificado con el número de cedula " + self._cedula + " tiene como funciones: supervisar el local, dirigir a los baristas y hacer uso correcto del sistema al que se le dio acceso"
    
    def getUsuario(self):
        return self._usuario
    
    def getContrasena(self):
        return self._contrasena
    
    def setUsuario(self, usuario):
        self._usuario = usuario
    
    def setContrasena(self, contrasena):
        self._contrasena = contrasena