import os, sys, time, socket

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as s:
        s.connect(("localhost", 8082))
    

        mensaje = "Dame la hora"
        
        s.send(mensaje.encode())
        print(s.recv(1024).decode())
        print(s.getsockname())
        print(s.getpeername())
        

if __name__ == "__main__":
    main()
