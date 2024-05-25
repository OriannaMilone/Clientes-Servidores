import os
import sys
import datetime
import socket as s 
#Servidor

def main():
    dir_socket_serv = '/tmp/socket_serv'
    if os.path.exists(dir_socket_serv):
        os.remove(dir_socket_serv)
    
    socket_servidor = s.socket(s.AF_UNIX,s.SOCK_STREAM)

    socket_servidor.bind(dir_socket_serv)          
    socket_servidor.listen() 
    
    while True:
         conexion, dir_cli  = socket_servidor.accept() #Esto es bloqueante
         fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n")
         conexion.send(fecha_actual.encode('utf-8'))
        # conexion.close()
    
    socket_servidor.close()
    #socket_servidor.shutdown(SHUT_WR)
if __name__ == '__main__':
    main()
