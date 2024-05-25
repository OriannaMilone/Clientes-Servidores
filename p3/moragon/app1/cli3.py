import os, sys

def crear_fifo(path_fifo):
    if not os.path.exists(path_fifo):
        os.mkfifo(path_fifo)


def main():
    if len(sys.argv) < 2:
        print("Numero invalido de parametros")
        return 1

    path_fichero = sys.argv[1] + "\n"

    path = "/tmp/fifo_servidor"
    path_2 = "/tmp/" + str(os.getpid())

    crear_fifo(path_2)

    #path_fichero = "./fichero.txt\n"

    with open(path, 'w') as fifo:
        fifo.write(path_fichero)
        fifo.flush()

        fifo.write(path_2)
        fifo.flush()
    
    with open(path_2, 'rb') as fifo2:
        #sys.stdout.write(fifo2.read())
        datos_bin = fifo2.read()
    try:
        sys.stdout.write(datos_bin.decode('utf-8'))
    except UnicodeDecodeError:
        sys.stdout = sys.stdout.detach()
        sys.stdout.write(datos_bin)

    os.remove(path_2)

if __name__ == "__main__":
    main()
