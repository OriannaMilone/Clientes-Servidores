import os, sys

def crear_fifo(path_fifo):
    if not os.path.exists(path_fifo):
        os.mkfifo(path_fifo)

def main():
    path = input("Indica la dirección del servidor: ")
    path_fifo2 = '/tmp/fifo2'
    with open(path, 'w') as fifo1:
        crear_fifo(path_fifo2)
        fifo1.write(path_fifo2)
        fifo1.flush()

    with open(path_fifo2, 'r') as fifo2:
        contenido =  fifo2.read()
        sys.stdout.write(contenido)

        os.remove(path_fifo2)
   
if __name__ == "__main__":
   main()

