import socket
import os
import datetime
import sys

def main():
   # direcc_socket = '0.0.0.0' # Escucha a todas las direcc
    direcc_socket = '127.0.0.1' 
    pr4_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    pr4_socket.bind((direcc_socket, 0))
    
    print("============================/n")
    direcc_local = pr4_socket.getsockname()
    print(f'la dirección local es {direcc_local}')
        

    
    while True:
        
        data, direcc_cli = pr4_socket.recvfrom(1024)

        with open(data.decode(), 'r') as file:
                contenido = file.read()
                pr4_socket.sendto(contenido.encode(), direcc_cli)  

if __name__ == "__main__":
    main()

