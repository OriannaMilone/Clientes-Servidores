import socket

class Servidor:
    def __init__(self, puerto):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
        self.s.bind(("0.0.0.0", puerto))
        self.cod = 'utf-8'

    def tratar_peticion(self):
        while True:
            path, addr = self.s.recvfrom(1024)
            contenido = self.obtener_contenido(path.decode(self.cod))
            self.s.sendto(contenido.encode(self.cod), addr)
            print("ENVIADO\n\n")

        self.s.close()

    def obtener_contenido(self, path):
        with open(path, 'r') as fd:
            contenido = fd.read()

        return contenido


if __name__ == '__main__':
    Servidor(8080).tratar_peticion()


