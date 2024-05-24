import unittest 
import serv7 as serv
import hashlib
import os

def buscar_credenciales(fichero, nombre, contrasenna=None) -> bool:
    with open(fichero, 'r') as f:
        contenido = f.read()

    if contrasenna:
        return (("\"" + nombre + "\", " + contrasenna + "\n") in contenido)
    else:
        return (("\"" + nombre + "\"") in contenido)

class ServidorTest(unittest.TestCase):

    # Test de prueba del entorno de trabajo (TDD)
    def test_true(self):
        self.assertTrue(True)

    # Test para comprobar un feedback de la autentificacion
    def test_autentificacion_devuelve_bool(self):
        tipo = type(serv.autentificar_cliente("Hola", "Quetal1234"))
        self.assertEqual(bool, tipo)
    
    # Test para definir el algoritmo de encriptacion usado para contrasenna
    def test_encriptacion_de_contrasenna(self):
        contrasenna = 'practica7'
        contrasenna_encriptada = hashlib.sha256(contrasenna.encode()).hexdigest()
        self.assertEqual(
                serv.encriptar_contrasenna(contrasenna),
                contrasenna_encriptada
                )
    
    # Te da un feedback de si se ha guardado correctamente
    def test_guardar_credenciales(self):
        salida = serv.guardar_credenciales("grupo 2", "practica7")
        self.assertEqual(bool, type(salida))
    

            

    def test_guardado_en_fichero(self):
        nombre = "grupo 2.1"
        contrasenna = "practica7"
        contrasenna_enc = serv.encriptar_contrasenna(contrasenna)
        fichero = "credenciales.csv"

        serv.guardar_credenciales(nombre, contrasenna)

        self.assertTrue(
                buscar_credenciales(fichero, nombre, contrasenna_enc)
                )
        

    def test_borrar_credenciales(self):
        nombre = "grupo 2.2"
        fichero = "credenciales.csv"

        serv.guardar_credenciales(nombre, "aaaa")

        serv.borrar_credenciales("grupo 2.2")

        self.assertFalse(
                buscar_credenciales(fichero, nombre)
                )
        
        

if __name__ == '__main__':
    unittest.main()
