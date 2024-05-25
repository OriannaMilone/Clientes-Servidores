import os, time, datetime, socket

def calcular_fecha():
    fecha_hora_actual = datetime.datetime.now()

    cadena_fecha_hora = fecha_hora_actual.strftime('%Y-%m-%dT%H:%M:%S%z')
    return cadena_fecha_hora

def main():
    try:
        os.unlink("/tmp/socket")
    except OSError:
        pass

    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM, 0) as s:
        s.bind("/tmp/socket")
        
        while True:
            s.listen()
            
            conn, addr = s.accept()
            with conn:
                    datos = conn.recv(1024)
                    conn.send(calcular_fecha().encode())

if __name__ == '__main__':
    main()
