import socket as s
import sys
import select 

class Cliente():
    def __init__(self):
        self.direccion = '127.0.0.1'
        self.puerto = 16021

        try:
            self.nick = sys.argv[1]
            self.password = sys.argv[2]
        except IndexError:
            sys.stdout.write("Se requieren dos argumentos: nick y password\n")
            sys.exit(1)

    def main(self):
        sock_cli = s.socket(s.AF_INET, s.SOCK_STREAM)
        sys.stdout.write('\nSolicitando Conexión\n')
        
        try:
            sock_cli.connect((self.direccion, self.puerto))
            sys.stdout.write('\nConectado al chat\n')
            lista_sockets = [sys.stdin, sock_cli]
            # Supuesta autenticación (enviar nick y password)
            # sock_cli.send(f"{self.nick} {self.password}".encode('utf-8'))

            while True:
                socket_listo, _, _ = select.select(lista_sockets, [], [])
                try:
                    for sock in socket_listo:
                        if sock == sock_cli:
                            mensaje_recv = sock_cli.recv(4096)
                            if mensaje_recv:
                                mensaje_recv = mensaje_recv.decode('utf-8')
                                sys.stdout.write(mensaje_recv + '\n')
                        else:
                            #mensaje_enviar = input('> ')
                            mensaje_enviar = sys.stdin.readline()
                            sys.stdout.write('> ')
                            sock_cli.send(mensaje_enviar.encode('utf-8'))

                except (ConnectionResetError, BrokenPipeError):
                    sys.stdout.write('\nEl servidor ha cerrado la conexión\n')
                    break
        except KeyboardInterrupt:
            sys.stdout.write("\nCliente detenido por el usuario\n")
        except ConnectionRefusedError:
            sys.stdout.write("\nNo se pudo conectar al servidor\n")
        finally:
            sock_cli.close()
            sys.stdout.write('Se ha cerrado la conexión\n')

if __name__ == '__main__':
    cli = Cliente()
    cli.main()

