import socket
import sys
import time


class server():
    def __init__(self):
        self.host = 'localhost'
        self.port = 65432

# Crear un socket UDP
    def main(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind((self.host, self.port))
            print(f"Servidor UDP en {self.host}:{self.port}")
            message, dir = s.recvfrom(1024)
            if message.decode().upper() == 'SI':
                print("Se ha cerrado el servidor UDP.")
                s.close()
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.bind(('localhost', self.port+1))
                    sock.listen()
                    while True:
                        print(f"Servidor TCP en {self.host}:{self.port+1}")
                        client_s, dir = sock.accept()
                        print(f'El cliente {dir} se ha conectado al servidor TCP')
                        while True:
                            decision_cls = client_s.recv(1024).decode() # ERROR DESPUES DE MORIR
                            print(decision_cls)
                            try:
                                if decision_cls == 'MORIR':
                                    print(f'El usuario {dir} ha cometido suicidio')
                                    client_s.sendall('Has decidido morir y desconectarte'.encode())
                                    client_s.close()
                                    break
                                else:
                                    print(f'El servidor ha declarado a {dir} gei')
                                    client_s.sendall('Vives siendo gei'.encode())
                            except KeyboardInterrupt:
                                print("Cerrandose...")
            else:
                sms, dir2 = s.recvfrom(4096)
                sys.stdout.write(sms.decode())
                print('\n')


if __name__ == "__main__":
    servidor = server()
    servidor.main()