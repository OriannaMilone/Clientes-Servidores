import os, sys, time

def crear_fifo(path_fifo):
    if not os.path.exists(path_fifo):
        os.mkfifo(path_fifo)

def main():
    path = "/tmp/fifo_servidor"
    path_2 = "/tmp/" + str(os.getpid())
    crear_fifo(path_2)

    # Abrimos pipe
    with open(path, 'w') as fifo:
        fifo.write(path_2)
        fifo.flush()

    with open(path_2, 'r') as fifo2:
        sys.stdout.write(fifo2.read())

    os.remove(path_2)
    


if __name__ == "__main__":
    main()
