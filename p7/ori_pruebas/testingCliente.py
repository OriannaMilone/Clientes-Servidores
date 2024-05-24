#TDD para eel Cliente
import clienterepaso as cli
import unittest
import re

class ClienteTest(unittest.TestCase):
   
    def setUp(self):
        self.client = cli.Cliente()
    
  #  def test_peticiones_extraordinarias(self):
   #     peticion = captar_peticion(#Quiero meter aqui algo como una interrupcion del teclado )
    #    self.assertTrue('Mensaje raro', peticion) #No se como (ChatGPT manda mocks)

#@patch('builtins.input', side_effect=KeyboardInterrupt)
 #   def test_peticiones_extraordinarias(self, mocked_input):
  #      with self.assertRaises(KeyboardInterrupt):
   #         self.client.captar_peticion() 

    def test_peticiones_minimas(self):
        peticiones_min_serv = self.client.cantidad_peticiones(4) 
        self.assertGreaterEqual(peticiones_min_serv, 3)

    #Otro test para asegurar que sea un int

if __name__ == '__main__':
    unittest.main()

