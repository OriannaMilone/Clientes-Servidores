import unittest
from unittest.mock import patch
from serv7 import crear_grupo_privado, comandos_del_cliente, enviar_mensaje_al_grupo

def mock_enviar_mensaje_a_cliente(conexion, mensaje):
        print(f'==> Mock: {conexion} - {mensaje}')
        return True

def mock_enviar_mensaje_a_todos(mensaje, conexiones):
    for cliente in conexiones:
        print("Mensaje enviado a " + str(cliente))
    return True


class TestServidor(unittest.TestCase):
    
    """
    Para crear un grupo:
    paloma: $$grupo: 1234
    jose: $$grupo: 1234
    se unirán al mismo grupo
    """
    
    def test_crear_un_grupo(self):
        grupos = {}
        data = "paloma: $$grupo 1234"
        conexion = "conexion_paloma"
        grupo_privado = crear_grupo_privado(conexion, data, grupos)
        self.assertEqual("1234", grupo_privado["conexion_paloma"])

    @patch('serv7.enviar_mensaje_a_cliente', side_effect=mock_enviar_mensaje_a_cliente)
    def test_comandos_del_cliente_crear_grupo(self, mocked_enviar_mensaje_a_cliente):
        data = "paloma: $$grupo: 1234"
        conexion = "conexion_paloma"
        grupos = {}
        resultado = comandos_del_cliente(data,conexion, grupos)
        self.assertTrue(resultado)

    """
    Para hablar por un grupo:
    paloma: $$send nombre_grupo mensaje_a_enviar
    """
        
    @patch('serv7.enviar_mensaje_a_todos', side_effect=mock_enviar_mensaje_a_todos)
    def test_enviar_mensaje_a_un_grupo(self, mock_enviar_mensaje_a_todos):
        mensaje = "paloma: $$send 1234 hola grupo!!!!"
        conexion = "conexion_paloma"
        grupos = {
                    "conexion_paloma": "1234",
                    "conexion_carlos": "1234",
                    "conexion_ori": "helou"
                }
        resultado = enviar_mensaje_al_grupo(mensaje, conexion, grupos)
        self.assertTrue(resultado)


    @patch('serv7.enviar_mensaje_a_todos', side_effect=mock_enviar_mensaje_a_todos)
    def test_comandos_del_cliente_enviar_mensaje_grupo(self, mock_enviar_mensaje_a_todos):
        mensaje = "paloma: $$send 1234 hola grupo!!!!"
        conexion = "conexion_paloma"
        grupos = {
                    "conexion_paloma": "1234",
                    "conexion_carlos": "1234",
                    "conexion_ori": "helou"
                }
        resultado = comandos_del_cliente(mensaje, conexion, grupos)
        self.assertTrue(resultado)
