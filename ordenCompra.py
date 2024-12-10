from calcularImpuesto import CalculadorImpuestos

class OrdenCompra:
    def __init__(self, productos):
        self._productos = productos
        self._calculador = CalculadorImpuestos()
    
    def get_productos(self):
        return self._productos
    
    def listar_productos(self):
        return self._productos
    
    def calcular_precio_final(self, estado):
        if len(estado) != 2:
            raise ValueError("El estado debe ser un código de 2 letras")
            
        costo = sum(producto.get_precio() for producto in self._productos)
        impuesto = self._calculador.calcular_impuesto(estado, costo)
        
        return costo + impuesto