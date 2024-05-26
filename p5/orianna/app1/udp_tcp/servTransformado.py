#Codigo Servidor
import socket as s

class Servidor():
    def __init__(self):
        self.direccion = '0.0.0.0'
        self.puerto = 16021
        self.puerto2 = 16022

    def main(self):
        sock_serv = s.socket(s.AF_INET, s.SOCK_DGRAM)
        sock_serv.bind((self.direccion, self.puerto))
        
        sock_sev2 = s.socket(s.AF_INET, s.SOCK_STREAM)

        try:
           peticion, remitente = sock_serv.recvfrom(4096)
           
           if peticion.decode('utf-8').lower() == 'TCP':
                sys.stdout.write('\nMatando al sock de UDP anterior\n')
                sock_serv.close()
                sys.stdout.write('\nMuerto UDP\n')
                sock_serv2.bind((self.direccion, self.puerto2))
                
                sock_serv2.listen(2)
                
                try:
                    while True:
                        sock_cli, sock_dir = sock_serv2.accept()
                        try:
                            mensaje = '\nServidor desde TCP: Hola!\n'
                            sock_cli.send(mensaje.encode('utf-8'))
                        except BrokenPipeError:
                             sys.stdout.write("El cliente se ha desconectado\n") 
                        finally:
                            sock_cli.close()
                except KeyboardInterrupt:
                    sys.stdout.write("\nServidor detenido por el usuario\n")
                finally:
                    sock_serv2.close()

                sys.stdout.write('Se ha cerrado la conexion\n')
            else:
                mensaje = '\nServidor UDP: Hola!\n'
                sock_serv.sendto(mensaje.encode('utf-8'),remitente)
        
        finally:
            sock_serv.close()

if __name__ == '__main__': 
    serv = Servidor()
    serv.main()
