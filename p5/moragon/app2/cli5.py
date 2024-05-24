import os, sys, time, socket

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0) as s:
        mensaje = "Dame la hora"

        s.sendto(mensaje.encode(), ("127.0.0.1", 8080))
        contenido, addr = s.recvfrom(1024)
        print(contenido.decode())

if __name__ == "__main__":
    main()
