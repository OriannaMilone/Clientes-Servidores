#Codigo Servidor
import socket as s

class Servidor():
    def __init__(self):
        self.direccion = '0.0.0.0'
        self.puerto = 16021
    
    def main(self):
        sock_serv = s.socket(s.AF_INET, s.SOCK_DGRAM)
        sock_serv.bind((self.direccion, self.puerto))
        #sock_serv.listen()
        #while True:
        #   sock_serv.accept()
            
        peticion, remitente = sock_serv.recvfrom(4096)
        #   peticion  = sock_serv.recv(4096)

        if peticion:
            sys.stdout.write('\nSe ha recibido una petición\n')
            mensaje = '\nSoy el Servidor: Hola!\n'
            sock_serv.sendto(mensaje.encode('utf-8'),remitente)
            #sock_serv.send(mensaje.encode('utf-8'))
        sock_serv.close()

if __name__ == '__main__': 
    serv = Servidor()
    serv.main()
