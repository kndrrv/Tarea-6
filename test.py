import unittest
from producto import Producto
from ordenCompra import OrdenCompra

class Compras(unittest.TestCase):
    def setUp(self):
        self.producto1 = Producto("Teclado", "TCD001", 1200.0)
        self.producto2 = Producto("Mouse", "MOU001", 20.0)
        self.productos = [self.producto1, self.producto2]
        self.orden = OrdenCompra(self.productos)
        
    def test_validacion_estado(self):
        # Prueba estado inválido (más de 2 letras)
        with self.assertRaises(ValueError):
            self.orden.calcular_precio_final("XXX")
            
    def test_calculo_impuestos(self):
        # Prueba NH (sin impuestos)
        self.assertEqual(self.orden.calcular_precio_final("NH"), 1220.0)
        
        # Prueba MA (18%)
        self.assertEqual(self.orden.calcular_precio_final("MA"), 1439.6)  # 1220 + (1220 * 0.18)
        
        # Prueba estado normal (15%)
        self.assertEqual(self.orden.calcular_precio_final("FL"), 1403.0)  # 1220 + (1220 * 0.15)

        # Pruebas para IL
        # Menos de 1000
        orden_pequena_il = OrdenCompra([Producto("Mouse", "MOU001", 500.0)])
        self.assertEqual(orden_pequena_il.calcular_precio_final("IL"), 500.0)  # Sin impuesto
        
        # Entre 1000 y 10000 (12%)
        orden_mediana_il = OrdenCompra([Producto("Laptop", "LAP001", 5000.0)])
        self.assertEqual(orden_mediana_il.calcular_precio_final("IL"), 5600.0)  # 5000 + (5000 * 0.12)
        
        # Más de 10000 (16%)
        orden_grande_il = OrdenCompra([Producto("Servidor", "SRV001", 15000.0)])
        self.assertEqual(orden_grande_il.calcular_precio_final("IL"), 17400.0)  # 15000 + (15000 * 0.16)

        # Pruebas para KY
        # Menos de 1000
        orden_pequena_ky = OrdenCompra([Producto("Mouse", "MOU001", 500.0)])
        self.assertEqual(orden_pequena_ky.calcular_precio_final("KY"), 500.0)  # Sin impuesto
        
        # Entre 1000 y 10000 (13%)
        orden_mediana_ky = OrdenCompra([Producto("Laptop", "LAP001", 5000.0)])
        self.assertEqual(orden_mediana_ky.calcular_precio_final("KY"), 5650.0)  # 5000 + (5000 * 0.13)
        
        # Más de 10000 (17%)
        orden_grande_ky = OrdenCompra([Producto("Servidor", "SRV001", 15000.0)])
        self.assertEqual(orden_grande_ky.calcular_precio_final("KY"), 17550.0)  # 15000 + (15000 * 0.17)
        
    def test_calculo_precio_final(self):
        # Verifica el cálculo del precio final
        self.assertEqual(self.orden.calcular_precio_final("NH"), 1220.0)  # Sin impuestos
        self.assertEqual(self.orden.calcular_precio_final("MA"), 1439.6)  # 1220 + (1220 * 0.18)
        self.assertEqual(self.orden.calcular_precio_final("FL"), 1403.0)  # 1220 + (1220 * 0.15)

        # IL (escalonado)
        orden_mediana_il = OrdenCompra([Producto("Laptop", "LAP001", 5000.0)])
        self.assertEqual(orden_mediana_il.calcular_precio_final("IL"), 5600.0)   # 15000 + (15000 * 0.16)

if __name__ == '__main__':
    unittest.main()