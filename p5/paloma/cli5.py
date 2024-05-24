import socket
import sys

def main():
    direcc_serv = '127.0.0.1'
    puerto = input("Introduzca el puerto de su servidor: ")
    cli_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    mensaje = input("Introduce la dirección del archivo a enviar: ")

    cli_socket.sendto(mensaje.encode(),(direcc_serv,int(puerto)))
    
    direcc_local = cli_socket.getsockname()
    # No hay conexion! -->  direcc_remota = cli_socket.getpeername()

    print(f'la dirección local es {direcc_local}')
        
    respuesta = cli_socket.recv(1024)

    print("Respuesta del servidor:\n", respuesta.decode())

   
if __name__ == "__main__":
    main()

# Ejemplo: /etc/libreoffice/registry/main.xcd
