#Código Servidor
import socket as s
import select 
import sys 

class Servidor():

    def __init__(self):
        self.direccion = '0.0.0.0'
        self.puerto = 16021
        self.usuarios_registrados = {}
        self.usuarios_conectados = []
    
    def clasificador_usuario(self, usuario_esperando, nick_usuario):
        if nick_usuario in self.usuarios_registrados:
            return 'Paso 2: Autentificacion'
        else:
            return 'No Registrado'

    def registrar_usuario(self, nick_usuario, contraseña):
        self.usuarios_registrados[nick_usuario] = contraseña
        return nick_usuario

    def login(self, nick_usuario, contraseña): 
        if self.usuarios_registrados[nick_usuario] == contraseña:
            self.usuarios_conectados.append(nick_usuario)
            return True
        else:
            return 'Contraseña Incorrecta'

    def main(self):
        lista_solicitudes = []
        mensajes = []
        num_conexiones_max = input('Indique el numero de conexiones máximas que desea\n> ')
        sock_serv = s.socket(s.AF_INET, s.SOCK_STREAM)
        sock_serv.bind((self.direccion, self.puerto))
        
        sys.stdout.write('Servidor Levantado\n')
        sock_serv.listen(int(num_conexiones_max))
        lista_solicitudes.append(sock_serv)
        #Ahora mismo los acepto a todos
        try:
            while True:
                usuarios_esperando, _, _ = select.select(lista_solicitudes.copy(), [], [])
                try:
                    for user in usuarios_esperando:
                        sock_cli, dir_cli = user.accept()
                        self.usuarios_conectados.append(sock_cli)
               
                    for user in self.usuarios_conectados:
                        mensaje = user.recv(4096).decode('utf-8')
                        if mensaje:
                            mensajes.append(mensaje)
                        for sms in mensajes:
                            user.send(sms.encode('utf-8'))
                except BrokenPipeError:
                    sys.stdout.write("El cliente se ha desconectado\n")
                finally: 
                    for user in self.usuarios_conectados:
                        user.close()
        except KeyboardInterrupt:
            sys.stdout.write("\nServidor detenido por el usuario\n")
        finally:
            sock_serv.close()
        
        sys.stdout.write('Se ha cerrado la conexion\n')



if __name__ == '__main__':
    serv = Servidor()
    serv.main()

