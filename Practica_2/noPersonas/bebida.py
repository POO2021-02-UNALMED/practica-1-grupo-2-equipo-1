class Bebida:
    
    def __init__(self, codigo, precio):
        self._codigo = codigo
        self._precio = precio
    
    def __str__(self):
        return 'La bebida preparada tiene un precio de ' + self.precio
        
    def getCodigo(self):
        return self._codigo
    
    def getPrecio(self):
        return self._precio
    
    def setCodigo(self, codigo):
        self._codigo = codigo
    
    def setPrecio(self, precio):
        self._precio = precio
    
    def fueVendido():
        pass