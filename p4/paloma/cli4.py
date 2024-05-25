import socket
import sys

def main():
    # server_address = '/tmp/socket_pr4'
    direcc_serv = sys.argv[1]

    cli_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    cli_socket.connect(direcc_serv)
    
    direcc_local = cli_socket.getsockname()
    direcc_remota = cli_socket.getpeername()
    print(f'la dirección local es {direcc_local} y la remota {direcc_remota}')

    mensaje = input("Introduce el mensaje a enviar: ")

    cli_socket.sendall(mensaje.encode())
        
    respuesta = cli_socket.recv(1024)

    """
        respuesta = b""
        while True:
            parteMensaje = cli_socket.recv(1024)
            if not parteMensaje:
                break
            respuesta += parteMensaje
    """
    print("Respuesta del servidor:", respuesta.decode())

    cli_socket.close()

if __name__ == "__main__":
    main()

