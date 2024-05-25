import socket
import sys

def main():
    # server_address = '/tmp/socket_pr4'
    direcc_serv = sys.argv[1]

    cli_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    cli_socket.connect(direcc_serv)
    
    direcc_local = cli_socket.getsockname()
    direcc_remota = cli_socket.getpeername()
    print(f'La dirección local es {direcc_local} y la remota {direcc_remota}')

    try:
        while True:
            mensaje = input("Introduce el mensaje a enviar (o 'salir' para terminar): ")
            if mensaje.lower() == 'salir':
                break

            cli_socket.sendall(mensaje.encode())
            
            respuesta = cli_socket.recv(1024)
            print("Respuesta del servidor:", respuesta.decode())
    except Exception as e:
        print(f"Error durante la comunicación: {e}")
    finally:
        cli_socket.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python cli4Recurrente.py <direccion_del_servidor>")
        sys.exit(1)
    main()

