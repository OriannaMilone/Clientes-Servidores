import socket, sys

class Cliente:
    def __init__(self, addr, puerto, path):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
        self.direccion = (addr, puerto)
        self.path = path
        self.cod = 'utf-8'

    def gestionar_peticion(self):
        self.s.sendto(self.path.encode(self.cod), self.direccion)
        contenido = self.leer_contenido()

        print(contenido)
        self.s.close()

    def leer_contenido(self):
        contenido = ""
        while True:
            info, _ = self.s.recvfrom(1024)
            contenido += info.decode(self.cod)
            if len(info) < 1024:
                break

        return contenido

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Error en los parametros")
        sys.exit(1)
    Cliente('localhost', 8080, sys.argv[1]).gestionar_peticion()
