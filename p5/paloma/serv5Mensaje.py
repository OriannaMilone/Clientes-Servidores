import socket
import os
import datetime
import sys
import ast

def main():
   # direcc_socket = '0.0.0.0' # Escucha a todas las direcc
    direcc_socket = '127.0.0.1' 
    pr4_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    pr4_socket.bind((direcc_socket, 0))
    
    print("============================/n")
    direcc_local = pr4_socket.getsockname()
    print(f'la dirección local es {direcc_local}')
        

    try:
        while True:
        
            data, direcc_cli = pr4_socket.recvfrom(1024)
            sys.stdout.write("Mensaje del cliente: "+data.decode())
            data = ast.literal_eval(data.decode())
            tam_archivo = data[0]

            """
            with open(data[1], 'r') as file:
                    contenido = file.read()
                    pr4_socket.sendto(contenido.encode(), direcc_cli)  
            """

            with open(data[1],'rb') as file:
                bytes_enviados = 0
                while bytes_enviados < tam_archivo:
                    bloque = file.read(1024)
                    bytes_enviados += len(bloque) # Por si acaso len --> no orientado a conexion
                    pr4_socket.sendto(bloque, direcc_cli)
                    sys.stdout.write("\n ==> Bytes enviados: "+ str(bytes_enviados))

                sys.stdout.write("\n===> FIN >>  Puerto del servidor: "+ str(direcc_local))
                

    except KeyboardInterrupt:
        print("Cerrando el servidor...")
        pr4_socket.close()

if __name__ == "__main__":
    main()

