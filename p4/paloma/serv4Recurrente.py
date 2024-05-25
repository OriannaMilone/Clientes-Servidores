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
    pr4_socket.listen(1)  # Aceptará hasta 1 conexión pendiente mientras está ocupado manejando una conexión activa

    while True:
        connection, _ = pr4_socket.accept()
        try:
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                mensaje = data.decode()
                print("Mensaje recibido:", mensaje)

                if mensaje.lower() == 'salir':
                    print("Cliente ha terminado la comunicación.")
                    break

                response = calcular_fecha()
                connection.sendall(response.encode())
                print("Fecha y hora enviadas al cliente:", response)
        except Exception as e:
            print(f"Error durante la comunicación con el cliente: {e}")
        finally:
            connection.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python serv4Recurrente.py <direccion_del_socket>")
        sys.exit(1)
    main()

