import socket as s
import select
import sys

class Servidor():
    def __init__(self):
        self.direccion = '0.0.0.0'
        self.puerto = 16021
        self.usuarios_conectados = []
        self.lista_solicitudes = []

    def main(self):
        num_conexiones_max = input('Indique el numero de conexiones máximas que desea\n> ')
        sock_serv = s.socket(s.AF_INET, s.SOCK_STREAM)
        sock_serv.bind((self.direccion, self.puerto))
        sys.stdout.write('Servidor Levantado\n')

        sock_serv.listen(int(num_conexiones_max))
        self.lista_solicitudes.append(sock_serv)

        try:
            while True:
                usuarios_esperando, _, _ = select.select(self.lista_solicitudes, [], [])
                for user in usuarios_esperando:
                    if user is sock_serv:
                        sock_cli, dir_cli = sock_serv.accept()
                        self.usuarios_conectados.append(sock_cli)
                        self.lista_solicitudes.append(sock_cli)
                        sys.stdout.write(f'\nSe ha conectado: {dir_cli}\n')
                        welcome = '\nBienvenido al chat\n'
                        sock_cli.send(welcome.encode('utf-8'))
                    else:
                        try:
                            mensaje = user.recv(1024)
                            if mensaje:
                                mensaje =str(dir_cli)+ ' ' +  mensaje.decode('utf-8') + '\n'
                                sys.stdout.write(f'\nHa llegado un mensaje: {mensaje}\n')
                                for usuario in self.usuarios_conectados:
                                        usuario.sendall(mensaje.encode('utf-8'))
                            else:
                                raise ConnectionResetError
                        except (ConnectionResetError, BrokenPipeError):
                            sys.stdout.write("Cliente desconectado\n")
                            self.usuarios_conectados.remove(user)
                            self.lista_solicitudes.remove(user)
                            user.close()
        except KeyboardInterrupt:
            sys.stdout.write("\nServidor detenido por el usuario\n")
        finally:
            for user in self.usuarios_conectados:
                user.close()
            sock_serv.close()
            sys.stdout.write('Se ha cerrado la conexión\n')

if __name__ == '__main__':
    serv = Servidor()
    serv.main()
