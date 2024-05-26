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

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    try:
        cliente.connect((ip, 8080))
        print("------------------------\n")
    except Exception as e:
        print("Error al conectar con el servidor:", e)
        sys.exit()

    inputs = [cliente, sys.stdin]
    while True:
        leer_sockets, _, _ = select.select(inputs, [], [])
        
        for sock in leer_sockets:
            if sock == cliente:
                datos = cliente.recv(1024)
                if not datos:
                    print("Desconectado del servidor.")
                    cliente.close()
                    sys.exit()
                else:
                    print("->" + datos.decode('utf-8'))
            else:
                contenido = sys.stdin.readline().strip()
                mensaje = nombre + "@@" + contenido
                cliente.send(mensaje.encode('utf-8'))
                print("Se envia", flush = True)

if __name__ == "__main__":
    main()
