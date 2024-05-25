import os, time

def crear_fifo(path_fifo):
    if not os.path.exists(path_fifo):
        os.mkfifo(path_fifo)

def main():
    path = "/tmp/fifo_servidor"
    
    crear_fifo(path)
    
    while True: 
        with open(path, 'r') as fifo:
            path_fichero = fifo.readline().rstrip("\n")
            path_fifo_2 = fifo.readline().rstrip("\n")
    
        with open(path_fichero, 'rb') as file:
            content = file.read()
    
        with open(path_fifo_2, 'wb') as fifo2:
            fifo2.write(content)
            fifo2.flush()
    
    os.remove(path)

if __name__ == "__main__":
    main()
