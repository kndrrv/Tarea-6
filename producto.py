class Producto:
    def __init__(self, nombre, codigo, precio):
        self._nombre = nombre
        self._codigo = codigo
        self._precio = precio
    
    # Get
    def get_nombre(self):
        return self._nombre
    
    def get_codigo(self):
        return self._codigo
    
    def get_precio(self):
        return self._precio
    
    # Set
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def set_codigo(self, codigo):
        self._codigo = codigo
    
    def set_precio(self, precio):
        self._precio = precio