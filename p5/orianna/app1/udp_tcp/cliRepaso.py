#Codigo Cliente 
import socket as s
import sys 

#TCP comentado

class Cliente():
    def __init__(self):
        self.direccion = '127.0.0.1'
        self.puerto = 16021
    
    def main(self):
        sock_cli = s.socket(s.AF_INET, s.SOCK_DGRAM)
        #sock_cli = s.socket(s.AF_INET, s.SOCK_STREAM)

        #sock_cli.connect((self.direccion, self.puerto))

        mensaje = '\nSoy el Cliente. Saludame\n'i
        sock_cli.sendto(mensaje.encode('utf-8'), (self.direccion, self.puerto))
        sms, remitente = sock_cli.recvfrom(4096)
        #sock_cli.send(mensaje.decode('utf-8'))
        #sock_cli.recv(4096)

        sys.stdout.write(sms.decode('utf-8'))
        
        sock_cli.close()


if __name__ == '__main__':
    cli = Cliente()
    cli.main()
