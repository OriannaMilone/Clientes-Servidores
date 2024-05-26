import socket
from datetime import datetime

class Servidor():
    def __init__(self, puerto):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
        self.s.bind(('0.0.0.0', puerto))
        

    def calcular_fecha_hora(self):
        fecha_hora = datetime.now()
        str_fecha_hora = fecha_hora.strftime("Fecha: %Y-%m-%d\nHora: %H:%M:%S\n")
        return str_fecha_hora


    def tratar_peticion(self):
        while True:
            _, direccion = self.s.recvfrom(1024)
            fecha_hora = self.calcular_fecha_hora()

            self.s.sendto(fecha_hora.encode('utf-8'),direccion)


        self.s.close()


if __name__ == '__main__':
    Servidor(8080).tratar_peticion()


