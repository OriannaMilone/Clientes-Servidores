import socket
import sys
import os

def main():
    direcc_serv = '127.0.0.1'
    puerto = input("Introduzca el puerto de su servidor: ")
    cli_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    path = input("Introduce la dirección del archivo a enviar: ")
    estructura_mensaje = str([os.path.getsize(path), path])

    cli_socket.sendto(estructura_mensaje.encode(),(direcc_serv,int(puerto)))
    
    direcc_local = cli_socket.getsockname()
    print(f'la dirección local es {direcc_local}')
    
    """
    respuesta = cli_socket.recv(1024)
    print("Respuesta del servidor:\n", respuesta.decode())
    """
    bytes_recibidos = 0
    while bytes_recibidos < os.path.getsize(path):
        bloque, _ = cli_socket.recvfrom(1024)
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
