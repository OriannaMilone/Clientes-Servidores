import socket
import os
import datetime
import sys
import ast

def calcular_fecha():
    fecha_hora_actual = datetime.datetime.now()

    cadena_fecha_hora = fecha_hora_actual.strftime("%Y-%m-%dT%H:%M:%S%z")
    
    return cadena_fecha_hora

def main():
   # direcc_socket = '0.0.0.0' # Escucha a todas las direcc
    direcc_socket = '127.0.0.1' 
    pr4_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    pr4_socket.bind((direcc_socket, 0))
    pr4_socket.listen(1) # Es TCP!!

    print("============================")
    direcc_local = pr4_socket.getsockname()
    print(f'la dirección local es {direcc_local}')
        

    try:
        while True:
            conexion, direcc_cli = pr4_socket.accept()

            data, _ = conexion.recvfrom(1024) # de conexion!
            print("Mensaje del cliente: "+str(data))
            hora = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S%z")

            conexion.sendall(hora.encode())
        
        conexion.close()
                

    except KeyboardInterrupt:
        print("Cerrando el servidor...")
        pr4_socket.close()

if __name__ == "__main__":
    main()

