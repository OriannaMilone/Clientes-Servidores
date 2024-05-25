import socket
import os
import datetime
import sys

def calcular_fecha():
    fecha_hora_actual = datetime.datetime.now()
    cadena_fecha_hora = fecha_hora_actual.strftime("%Y-%m-%dT%H:%M:%S%z")
    return cadena_fecha_hora

def main():
    direcc_socket = sys.argv[1]
    print(f'La dirección del socket es: {direcc_socket}')
    # direcc_socket = '/tmp/socket_pr4'
    
    if os.path.exists(direcc_socket):
        try:
            os.unlink(direcc_socket)
        except OSError as e:
            print("No se puede eliminar el socket existente:", e)

    pr4_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    pr4_socket.bind(direcc_socket)
    pr4_socket.listen(1) # aceptará hasta 1 conexión pendiente mientras está ocupado manejando una conexión activa


    while True:
        connection, _ = pr4_socket.accept()
        
        data = connection.recv(1024)
        """
        while True:
            data = b""
            while True:
                parteMensaje = connection.recv(1)
                if not parteMensaje:
                    break
                data += parteMensaje
                break
        """
        print("Mensaje recibido:", data.decode())

        response = calcular_fecha()
        connection.sendall(response.encode())
        """
        data = connection.recv(4096)

        while data:
            print("Recibido:", data.decode())
            response = calcular_fecha()
            connection.sendall(response.encode())
        """
        print("============================/n")
        direcc_local = pr4_socket.getsockname()      
        print(f'la dirección local es {direcc_local}')

        connection.close()

if __name__ == "__main__":
    main()

