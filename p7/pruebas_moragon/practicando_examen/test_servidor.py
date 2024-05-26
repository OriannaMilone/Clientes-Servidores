import unittest
from servidor import Servidor
import re
class TestServidor(unittest.TestCase):

    def setUp(self):
        self.servidor = Servidor(8080)

    def test_guardan_el_puerto(self):
        self.assertEqual(self.servidor.puerto, 8080)
    
    def test_se_crea_el_socket(self):
        self.assertIsNotNone(self.servidor.s)

    def test_se_establecer_codificacion(self):
        self.assertEqual(self.servidor.codificacion, 'utf-8')

    def test_obtener_hora(self):
        hora = self.servidor.obtener_hora()
        self.assertEqual(str, type(hora))
    
    def test_formato_hora(self):
        self.assertEqual(self.servidor.formato_hora, "%H:%M:%S")

    
if __name__ == '__main__':
    unittest.main()
