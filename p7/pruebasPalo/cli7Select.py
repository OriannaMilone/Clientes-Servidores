import socket
import sys
import os
import select

def enviar_un_mensaje(cli_socket):
    mensaje = sys.stdin.readline().rstrip()
    estructura_mensaje = nick + ": " + mensaje

    cli_socket.send(estructura_mensaje.encode())

def recibir_mensaje_servidor(cli_socket):
    datos = cli_socket.recv(1024)
    return datos.decode()

def main():
    global nick
    direcc_serv = sys.argv[1]
    puerto = 8088
    cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli_socket.connect((direcc_serv, puerto))
    
    sys.stderr.write(f'Su dirección local es: {cli_socket.getsockname()}\n') 

    nick = input("Introduzca su nombre de usuario (nick): ")
    
    # Configurar la entrada estándar en modo no bloqueante
    sys.stdin = os.fdopen(sys.stdin.fileno(), 'r', 1)

    try:
        while True:
            ready_rlist, _, _ = select.select([cli_socket, sys.stdin], [], [])

            for sock in ready_rlist:
            
                if sock == cli_socket:
                    datos = recibir_mensaje_servidor(sock)
                    if datos == "$exit$": 
                        sock.close()
                        break
                    print(str(datos))
                    sys.stderr.write(datos)

                else:
                    enviar_un_mensaje(cli_socket)
    finally:
        print("Saliendo del chat...\n")
        cli_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write("Uso: python nombre_script.py <dirección_servidor>\n")
        sys.exit(1)
    main()

