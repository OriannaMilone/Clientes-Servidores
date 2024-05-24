import socket
import select
import sys

def main():
    
    if len(sys.argv) <4:
        print("Numero invalido de parametros")
        return 1

    nombre = sys.argv[1]
    password = sys.argv[2]
    ip = sys.argv[3]

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        cliente.connect((ip, 8080))
        print("------------------------\n")
    except Exception as e:
        print("Error al conectar con el servidor:", e)
        sys.exit()

    inputs = [cliente, sys.stdin]
    cliente.send((f"{nombre}|&|&|{password}").encode())
    while True:
        #outputs:  leer, escribir, excepciones
        #inputs: lo mismo pero son para monitorear
        leer_sockets, _, _ = select.select(inputs, [], [])
        
        for sock in leer_sockets:
            if sock == cliente:
                # Datos recibidos del servidor
                datos = cliente.recv(1024)
                if not datos:
                    print("Desconectado del servidor.")
                    cliente.close()
                    sys.exit()
                else:
                    usuario, mensaje = (datos.decode()).split("|&|&|")
                    print(f"<<{usuario}>> {mensaje}")
            else:
                mensaje = sys.stdin.readline().strip()
                mensaje = nombre + "|&|&|" + mensaje
                cliente.sendall(mensaje.encode())

if __name__ == "__main__":
    main()
