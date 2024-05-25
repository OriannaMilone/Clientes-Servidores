import os
import sys
import datetime
import socket as s 
#Servidor

def leer_archivo(ruta_archivo):
    contenido_archivo = '' 
    with open(ruta_archivo, 'r') as file:
            contenido_archivo = file.read()
    return contenido_archivo

def main():
    dir_socket_serv = '/tmp/socket_serv'
    if os.path.exists(dir_socket_serv):
        os.remove(dir_socket_serv)
    
    socket_servidor = s.socket(s.AF_UNIX,s.SOCK_STREAM)

    socket_servidor.bind(dir_socket_serv)          
    socket_servidor.listen() 
    
    #while True:
    conexion, dir_cli  = socket_servidor.accept() #Esto es bloqueante
    ruta_archivo = conexion.recv(4096)
    ruta_archivo = str(ruta_archivo.decode('utf-8'))
        
    contenido_archivo = leer_archivo(ruta_archivo)
    conexion.send(contenido_archivo.encode('utf-8'))
    conexion.close()
    
    socket_servidor.close()
    #socket_servidor.shutdown(SHUT_WR)
if __name__ == '__main__':
    main()
