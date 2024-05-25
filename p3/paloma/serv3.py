import os, time, datetime, sys

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
    print("La FIFO del servidor está en "+ path)
    
    while True:
        with open(path, 'r') as fifo1:  # abrir fifo1 modo lectura
            while True:
                path_fifo2 = fifo1.read()
                break    
        
            with open(path_fifo2, 'w') as fifo2:
                fifo2.write(calcular_fecha() + "\n")
                fifo2.flush() 

if __name__ == "__main__":
    main()
