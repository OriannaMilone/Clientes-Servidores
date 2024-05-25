import os

def main():
    print("Por ahora, la FIFO es /tmp/fifo_dreamTeam")
    path_fifo = input("Indique la ruta de la fifo: ")

    with open(path_fifo, 'r') as fifo:
        while True:
            # Leer datos del FIFO
            data = fifo.readline().strip()
            if data:
                print("Fecha y hora recibida del servidor:", data)
                break
            else:
                
                break

if __name__ == "__main__":
    main()

