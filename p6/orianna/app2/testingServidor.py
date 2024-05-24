#TDD para recepcion y emision de respuestas del servidor 
import servidorrepaso as serv
import unittest
import re

class ServidorFechas(unittest.TestCase):
   
    def setUp(self):
        self.servidor = serv.Servidor()
    
    def test_R_fecha_validas(self):
        respuesta_serv = self.servidor.respuesta_peticion('FECHA')
        regex_fecha = r"^\d{4}-\d{2}-\d{2}$"
        self.assertTrue(re.fullmatch(regex_fecha, respuesta_serv))

    def test_R_hora_validas(self): #Triangulando formato de peticion (minúculas)
        respuesta_serv = self.servidor.respuesta_peticion('hora')
        regex_hora = r"^\d{2}:\d{2}:\d{2}(?:\.\d+)?$"
        self.assertTrue(re.fullmatch(regex_hora, respuesta_serv))

    def test_responde_peticiones_malas(self):
        respuesta_serv = self.servidor.respuesta_peticion('nald94*_9d')
        self.assertTrue('ERROR\n', respuesta_serv)
       
if __name__ == '__main__':
    unittest.main()

