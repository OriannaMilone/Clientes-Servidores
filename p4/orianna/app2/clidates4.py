import os
import sys
import socket as s
#Cliente

def main():
    dir_socket_serv = '/tmp/socket_serv'
    socket_cliente = s.socket(s.AF_UNIX, s.SOCK_STREAM)
    #sys.stdout.write('\n')
    #sys.stdout.flush()

    socket_cliente.connect(dir_socket_serv)

    socket_cliente.send('Dame la hora'.encode('utf-8'))
    sys.stdout.write('Se ha enviado la peticion\n')
    sys.stdout.flush()
    
    data_recibida = socket_cliente.recv(4096)

    sys.stdout.write("Datos leídos del servidor:\n" + str(data_recibida.decode('utf-8')))
    
    #socket_cli.shutdown(SHUT_WR)
    socket_cliente.close()

if __name__ == '__main__':
    main()
