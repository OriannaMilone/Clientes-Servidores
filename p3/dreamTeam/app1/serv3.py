import os

def crear_fifo(path_fifo):
    if not os.path.exists(path_fifo):
        os.mkfifo(path_fifo)

def main():
    path_fifo = "/tmp/fifo_server"
    print("La fifo esta " + path_fifo)
    crear_fifo(path_fifo)
    
    # Abrimos pipe
    
    with open(path_fifo, 'w') as fifo:
        # Se debe pasar "'path'\npid"
        path = fifo.read().split("\n")[0]
        pid = fifo.read().split("\n")[1]

        with open(path, 'r') as file:
            crear_fifo("/tmp/"+pid)

            with open("/tmp/"+pid, 'w') as fifo2:
                fifo2.write(file.read())
                fifo2.flush()
    
    os.remove(path_fifo)
    # El fifo de respuesta lo cierra el cliente por ahora.

if __name__ == "__main__":
    main()
