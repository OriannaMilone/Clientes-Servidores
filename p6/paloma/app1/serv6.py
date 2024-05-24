import socket
import os
import datetime
import sys
import ast

def main():
   # direcc_socket = '0.0.0.0' # Escucha a todas las direcc
    direcc_socket = '127.0.0.1' 
    pr4_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    pr4_socket.bind((direcc_socket, 0))
    pr4_socket.listen(1) # Es TCP!!

    sys.stderr.write("============================")
    direcc_local = pr4_socket.getsockname()
    sys.stderr.write(f'la dirección local es {direcc_local}')
        

    try:
        while True:
            conexion, direcc_cli = pr4_socket.accept()

            data, _ = conexion.recvfrom(1024) # de conexion!
            sys.stdout.write("Mensaje del cliente: "+str(data))
            data = ast.literal_eval(data.decode())
            
            tam_archivo = data[0]

            with open(data[1],'rb') as file:
                bytes_enviados = 0
                while bytes_enviados < tam_archivo:
                    bloque = file.read(1024)
                    bytes_enviados += len(bloque) # Por si acaso len --> no orientado a conexion
                    conexion.sendall(bloque)
                    sys.stderr.write("\n ==> Bytes enviados: "+ str(bytes_enviados))

                sys.stderr.write("\n===> FIN >>  Puerto del servidor: "+ str(direcc_local))

            conexion.close()
                

    except KeyboardInterrupt:
        print("Cerrando el servidor...")
        pr4_socket.close()

if __name__ == "__main__":
    main()

