import unittest 
import servidorchat as servchat

class ServidorTesting(unittest.TestCase):
    
    def setUp(self):
        self.servidor = servchat.Servidor()
     
    def test_identifica_usuario(self):
        self.servidor.usuarios_registrados['orianna'] = 'contraseña1234'
        usuario_esperando = ('127.0.0.1', 16021)
        tipo_usuario = self.servidor.clasificador_usuario(usuario_esperando, 'orianna')
        self.assertEqual(tipo_usuario, 'Paso 2: Autentificacion')  
  
    def test_identificacion_usuario_2(self):
        usuario_esperando = ('127.0.0.1', 16021)
        tipo_usuario = self.servidor.clasificador_usuario(usuario_esperando, 'paloma')
        self.assertEqual(tipo_usuario, 'No Registrado')  
  

    def test_usuario_registra(self):
        usuario_esperando = ('127.0.0.1', 16021)
        nuevo_usuario = self.servidor.registrar_usuario('paloma', 'contraseña')    
        tipo_usuario = self.servidor.clasificador_usuario(usuario_esperando, nuevo_usuario)
        self.assertEqual(tipo_usuario,  'Paso 2: Autentificacion')
        
    def test_usuario_se_logea(self):
        self.servidor.usuarios_registrados['orianna'] = 'contraseña'
        self.assertTrue(self.servidor.login('orianna', 'contraseña'))
    


if __name__ == '__main__':
    unittest.main()
