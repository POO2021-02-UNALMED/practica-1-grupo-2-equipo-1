import random
class Domiciliario:
    _domiciliarios = []
    
    def __init__(self, nombre):
        id = random.randint(1000, 9000)
        self._codigo = id
        self._nombre = nombre
        self._incidentes = False
        Domiciliario._domiciliarios.append(self)
    
    def getNombre(self):
        return self._nombre

    def getCodigo(self):
        return self._codigo
    
    def isIncidentes(self):
        return self._incidentes
    
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def setCodigo(self, codigo):
        self._codigo = codigo
    
    def setIncidentes(self, incidentes):
        self._incidentes = incidentes
    
    @classmethod
    def getDomiciliarios(cls):
        return cls._domiciliarios

    @classmethod
    def setDomiciliarios(cls, domiciliarios):
        cls._domiciliarios = domiciliarios
    
    def __str__(self):
        incidentes = None
        
        if self._incidentes:
            incidentes = "este domiciliario ha sido reportado previamente"
        else:
            incidentes = "este domiciliario no ha sido reportado previamente"
        
        return "\nLa orden fue asignada a " + self._nombre +"\n" + incidentes
        