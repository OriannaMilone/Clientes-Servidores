#Código Cliente 
import socket as s
import sys

class Cliente():

    def __init__(self):
        self.direccion = '127.0.0.1' #Direccion calle
        self.puerto = 16031 #Direccion portal

    def recibir_respuesta(self, socket_servidor):
       peticion =  socket_servidor.recv(4096).decode('utf-8') 
       return peticion

    def enviar_peticion(self, socket_servidor):
        peticion = input('Escriba su peticion para el servidor\n> ')
        socket_servidor.send(peticion.encode('utf-8'))
        return 'Se ha enviado la peticion\n'
    
    def  establecer_conexion(self):
        sock_cli = s.socket(s.AF_INET, s.SOCK_STREAM)
        sock_cli.connect((self.direccion, self.puerto))
        return sock_cli, 'Cliente Iniciado\n'

    def cantidad_peticiones(self, num):
        #Cambiar nombre del test (Porque lo que hace es validar)
        if int(num) < 3:
            sys.stdout.write('Deben ser mínimo 3 peticiones (Trabajando con el valor por defecto "3")\n')
            return 3
        else: 
            return int(num)

    def main(self):
        sock_cli, estado = self.establecer_conexion()
        sys.stdout.write(estado)

        num = input('Escriba el numero de peticiones que desea hacer\n> ')
        num_peticiones = self.cantidad_peticiones(num)
        
        try:
            for i in range(num_peticiones):
                resultado = self.enviar_peticion(sock_cli)    
                sys.stdout.write(resultado)
                peticion = self.recibir_respuesta(sock_cli)
                sys.stdout.write(peticion)
        except KeyboardInterrupt:
                sys.stdout.write("\nCliente detenido por el usuario\n")
        finally:
                sock_cli.close()
                sys.stdout.write('Se ha cerrado la conexion\n')


if __name__ == '__main__':
    cli = Cliente()
    cli.main()

