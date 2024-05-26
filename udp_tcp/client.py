import socket
import time


class client():
    def __init__(self):
        self.host = 'localhost'
        self.port = 65432

    def main(self):
        # Crear un socket UDP
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            change_con = input("¿Solicita cambio de conexion? SI | NO: ")
            s.sendto(change_con.encode(), (self.host, self.port))
            if change_con.upper() == 'SI':
                s.close()
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    try:
                        time.sleep(1) # se conecta al servidor que no existe todavia sino
                        sock.connect(('localhost', self.port+1))
                        print(f'Te has conectado al servidor TCP {self.host}:{self.port+1}')

                        while True:
                            decission = input("Toma una decision 'MORIR' | 'VIVIR': ")
                            sock.send(decission.encode())
                            if decission == 'MORIR':
                                respuesta = sock.recv(1024).decode()
                                print(respuesta)
                                sock.close()
                                break
                            elif decission == 'VIVIR':
                                respuesta = sock.recv(1024).decode()
                                print(respuesta)
                            else:
                                print('ereh gei')

                    except ConnectionRefusedError:
                        print("Connection refused. Make sure the server is running.")
                    except KeyboardInterrupt:
                        print("Cerrandose...")
                    except Exception as e:
                        print(f"An error occurred: {e}")

            elif change_con.upper() == 'NO':
                s.sendto('Te has quedao anticuao.'.encode(), (self.host, self.port))
                print('Te has quedao anticuao.')

            else:
                print('Chupame el pito.')


if __name__ == "__main__":
    cliente = client()
    cliente.main()

