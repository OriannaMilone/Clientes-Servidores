import os, time, datetime

def calcular_fecha():
    fecha_hora_actual = datetime.datetime.now()

    cadena_fecha_hora = fecha_hora_actual.strftime("%Y-%m-%dT%H:%M:%S%z")
    return cadena_fecha_hora

def crear_fifo(path_fifo):
    if not os.path.exists(path_fifo):
        os.mkfifo(path_fifo)

def main():
    path = "/tmp/fifo_servidor"

    crear_fifo(path)
    while True:
        # Abrimos pipe
        with open(path, 'r') as fifo:
            path_2 = fifo.read()
    
        
        with open(path_2, 'w') as fifo_respuesta:
            fifo_respuesta.write(calcular_fecha() + "\n")
            fifo_respuesta.flush()
        
    os.remove(path)

if __name__ == "__main__":
    main()
