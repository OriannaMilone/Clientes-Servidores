import unittest

class TestServidor(unittest.TestCase):
    
    def setUp(self):
        servidor = self.Servidor()    

    def test_formato_fecha(self):
        fecha_respuesta = self.servidor.dar_fecha('FECHA')
        
        self.assertEqual(fecha_respuesta) #haga match con el formato 





if __name__ == '__main__':
    unittest.main()
