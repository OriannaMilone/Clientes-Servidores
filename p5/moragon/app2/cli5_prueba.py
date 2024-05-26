import socket

class Cliente:
    def __init__(self, addr, puerto):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
        self.direccion = (addr, puerto)
        self.cod = 'utf-8'
        self.hora = ''

    def gestionar_peticion(self):
        mensaje = ("dame la fecha y la hora").encode(self.cod)
        self.s.sendto(mensaje, self.direccion)
        self.hora, addr = self.s.recvfrom(1024)
        
        print(self.hora.decode(self.cod))
        
        self.s.close()
        

if __name__ == '__main__':
    Cliente("localhost", 8080).gestionar_peticion()
