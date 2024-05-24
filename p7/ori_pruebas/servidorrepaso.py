#Código Servidor
import datetime 
import socket as s
import sys

#Cosas a reviar: Cómo cerrar bien el socket
#                Qué pasa si el mensaje es más largo

class Servidor():
    def  __init__(self):
        self.direccion = '0.0.0.0' #Direccion calle
        self.puerto = 16031 #Direccion portal 

    def respuesta_peticion(self, peticion_cliente):
        if peticion_cliente.lower() == 'fecha':
            return datetime.datetime.now().date().strftime("%Y-%m-%d") + '\n'
        elif peticion_cliente.lower() == 'hora':
            fecha_hora_actual = datetime.datetime.now()
            hora = fecha_hora_actual.strftime("%H:%M:%S")
            return hora + '\n'
        else:
            return 'ERROR\n'

    def recibir_peticion(self, socket_cliente):
       peticion =  socket_cliente.recv(4096).decode('utf-8') #Averiguar como hacer lo del bucle / Porque marcadores de fin (creo que no necesito) 
       return peticion 

    def enviar_respuesta(self, respuesta_peticion, socket_cliente):
        respuesta_peticion = respuesta_peticion.encode('utf-8')
        socket_cliente.send(respuesta_peticion)
        return 'Se ha enviado la respuesta\n'

    def establecer_conexion(self):
        sock_serv = s.socket(s.AF_INET, s.SOCK_STREAM)
        sock_serv.bind((self.direccion, self.puerto))
        return sock_serv, 'Servidor Levantado\n'

    def main(self):
        sock_serv, estado = self.establecer_conexion()
        sys.stdout.write(estado)
        
        sock_serv.listen() # No se si esto va en el bucle
        
        try:
            while True:
                sock_cli, dir_cli = sock_serv.accept() 
                try:
                    while True:
                        peticion = self.recibir_peticion(sock_cli)
                        respuesta = self.respuesta_peticion(peticion)
                        resultado = self.enviar_respuesta(respuesta, sock_cli)
                        sys.stdout.write(resultado)
                #except ConnectionResetError:
                #    sys.stdout.write("El cliente se ha desconectado\n")
                except BrokenPipeError:
                    sys.stdout.write("El cliente se ha desconectado\n") #Esto es por no cerrar bien el socket 
                finally:
                    sock_cli.close()
        except KeyboardInterrupt: 
                sys.stdout.write("\nServidor detenido por el usuario\n")
        finally:
                sock_serv.close()
        
        sys.stdout.write('Se ha cerrado la conexion\n')



if __name__ == '__main__':
    serv = Servidor()
    serv.main()
