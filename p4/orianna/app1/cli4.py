import os
import sys
import socket as s
#Cliente

def main():
    dir_socket_serv = '/tmp/socket_serv'
    ruta_archivo = '/home/ped2/p4/orianna/app1/archivo_prueba.txt'
    socket_cliente = s.socket(s.AF_UNIX, s.SOCK_STREAM)

    socket_cliente.connect(dir_socket_serv)

    socket_cliente.send(ruta_archivo.encode('utf-8'))

    sys.stdout.write('Se ha enviado la ruta\n')
    sys.stdout.flush()
    
    respuesta_final = ''
    while True: 
         data_recibida = socket_cliente.recv(4096)
         if data_recibida:
            respuesta_final += str(data_recibida.decode('utf-8')) + ' '
         else:
             break

    sys.stdout.write("Datos leídos del servidor:\n" + respuesta_final)

    socket_cliente.close()

if __name__ == '__main__':
    main()
