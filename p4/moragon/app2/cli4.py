import os, sys, time, socket

def main():
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM, 0) as s:
        #s.bind("/tmp/socket")
        s.connect("/tmp/socket")
    

        mensaje = "Dame la hora"

        s.send(mensaje.encode())
        print(s.recv(1024).decode())

if __name__ == "__main__":
    main()
