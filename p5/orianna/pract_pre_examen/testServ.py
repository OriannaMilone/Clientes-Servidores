#Testing Servidor 
import unittest
import servidor as serv

class TestServidor(unittest.TestCase):
    
    def setUp(self):
        self.servidor = serv.Servidor()

    def test_clasificador_peticiones(self):
        resultado = self.servidor.clasificar_peticiones('Triangulo')
        self.assertEqual(resultado, 3)
    
    def test_clasificador_peticiones2(self):
        resultado = self.servidor.clasificar_peticiones('jfnrfs')
        self.assertEqual(resultado, 0)
       
    def test_area_triangulo(self):
        area_calculada = self.servidor.calcular_area(3, 4, 5, 0) #4 base | 5 altura
        self.assertEqual(area_calculada, 10)
    
    def test_area_circulo(self):
        area_calculada = self.servidor.calcular_area(1, 0, 0, 3)
        self.assertEqual(area_calculada, 28)
    
    def test_perimetro_rectangulo(self):
        perimetro = self.servidor.calcular_perimetro(2,4)
        self.assertEqual(perimetro, 12)


if __name__ == '__main__':
    unittest.main()
