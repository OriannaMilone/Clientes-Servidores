import socket
import sys
import os

def main():
    direcc_serv = '127.0.0.1'
    puerto = input("Introduzca el puerto de su servidor: ")
    cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli_socket.connect((direcc_serv, int(puerto)))


    path = input("Introduce la dirección del archivo a enviar: ")
    estructura_mensaje = str([os.path.getsize(path), path])

    cli_socket.sendall(estructura_mensaje.encode()) # Cambiamos a sendall!
    
    direcc_local = cli_socket.getsockname()
    sys.stdout.write(f'la dirección local es {direcc_local}')
    
    bytes_recibidos = 0
    while bytes_recibidos < os.path.getsize(path):
        bloque = cli_socket.recv(1024) #recv no recvfrom!
        bytes_recibidos += 1024
        sys.stdout.write(bloque.decode())
  
    sys.stdout.write("==>Fin\n")


if __name__ == "__main__":
    main()

# Ejemplo: /etc/libreoffice/registry/main.xcd

"""
Vamos a crear una estructura de Mensaje:
Vamos a enviar una lista:
    [Tamaño archivo, path_archivo]
"""
