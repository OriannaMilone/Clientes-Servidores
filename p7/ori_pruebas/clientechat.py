#Código Cliente
import socket as s
import sys

class Cliente():
    def __init__(self):
        self.direccion = '127.0.0.1'
        self.puerto = 16021
         
        try:
            self.nick = sys.argv[1]
            self.password = sys.argv[2]
        except IndexError: 
            sys.stdout.write("Se requieren dos argumentos: nick y password")
            sys.exit(1)

    def main(self):
        sock_cli = s.socket(s.AF_INET, s.SOCK_STREAM)
        sys.stdout.write('\nSolicitando Conexion\n')
        
        sock_cli.connect((self.direccion, self.puerto))
        sys.stdout.write('\nConectado al chat\n')

        #Se tiene que autentificar supuestamente
        
        try:
            while True:
                mensaje_recv = sock_cli.recv(4096).decode('utf-8')
                if mensaje_recv:
                    sys.stdout.write(mensaje_recv)
                mensaje_enviar = input('> ')
                sock_cli.send(mensaje_enviar.encode('utf-8'))
        except KeyboardInterrupt: 
               sys.stdout.write("\nCliente detenido por el usuario\n")
        except BrokenPipeError:
                sys.stdout.write('\nEl servidor ha cerrado la conexion\n')
        finally:
                sock_cli.close()

        sys.stdout.write('Se ha cerrado la conexion\n')




if __name__ == '__main__':
    cli = Cliente()
    cli.main()
