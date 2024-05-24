import os, sys, socket, struct

def main():
    if len(sys.argv) < 2:
        print("Numero invalido de parametros")
        return 1

    path_fichero = sys.argv[1]

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0) as s:
        s.sendto(path_fichero.encode(), ("127.0.0.1", 8081))

        datos_bin = b''

        while True:
            mensaje_completo, _ = s.recvfrom(1024)

            cabecera = mensaje_completo[:4]

            tamaño = struct.unpack('!I', cabecera)[0]
            
            datos_bin += mensaje_completo[4:]

            if tamaño == 0:
                break
            


    try:
        sys.stdout.write(datos_bin.decode('utf-8'))
    except UnicodeDecodeError:
        sys.stdout = sys.stdout.detach()
        sys.stdout.write(datos_bin)

if __name__ == "__main__":
    main()
