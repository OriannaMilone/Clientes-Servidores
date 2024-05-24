import os, time, socket

def leerfichero(path_fichero):
    with open(path_fichero, 'rb') as file:
        return file.read()

def main(): # Delegar en un hijo para /dev/null
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as s:
        s.bind(("0.0.0.0", 8086))
        
        while True:
            s.listen()
            
            conn, addr = s.accept()
            with conn:
                    datos = conn.recv(1024).decode()
                    conn.send(leerfichero(datos))

if __name__ == '__main__':
    main()
