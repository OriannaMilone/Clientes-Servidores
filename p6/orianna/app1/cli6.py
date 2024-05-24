import os
import sys
import socket as s
#Cliente

def main():
    dir_socket_serv = '0.0.0.0'
    puerto_socket_serv = 1026

    ruta_archivo = '/home/ped2/p6/orianna/app1/archivo_prueba.txt'

    socket_cliente = s.socket(s.AF_INET, s.SOCK_STREAM)
    destino = (dir_socket_serv, puerto_socket_serv)
    
    socket_cliente.connect(destino)

    socket_cliente.send(ruta_archivo.encode('utf-8'))

    sys.stdout.write('Se ha enviado la ruta\n')
    sys.stdout.flush()
    
    respuesta_final = socket_cliente.recv(4096) #Para esto que es pqueño si alcanza
    sys.stdout.write("Datos leídos del servidor:\n" + respuesta_final.decode('utf-8'))
    socket_cliente.close()

if __name__ == '__main__':
    main()
