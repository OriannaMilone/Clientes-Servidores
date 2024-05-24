import os, time, datetime, socket

def calcular_fecha():
    fecha_hora_actual = datetime.datetime.now()

    cadena_fecha_hora = fecha_hora_actual.strftime('%Y-%m-%dT%H:%M:%S%z')
    return cadena_fecha_hora

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0) as s:
        s.bind(("0.0.0.0", 8080))
        
        while True:
            datos, addr = s.recvfrom(1024)
            s.sendto(calcular_fecha().encode(), addr)

if __name__ == '__main__':
    main()
