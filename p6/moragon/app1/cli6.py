import os, sys, socket

def main():
    if len(sys.argv) < 2:
        print("Numero invalido de parametros")
        return 1

    path_fichero = sys.argv[1]

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as s:
        s.connect(("0.0.0.0", 8086))
        
        s.send(path_fichero.encode())

        datos_bin = b''

        while True:
            datos = s.recv(1024)
            if not datos:
                break

            datos_bin += datos

    try:
        sys.stdout.write(datos_bin.decode('utf-8'))
    except UnicodeDecodeError:
        sys.stdout = sys.stdout.detach()
        sys.stdout.write(datos_bin)

if __name__ == "__main__":
    main()
