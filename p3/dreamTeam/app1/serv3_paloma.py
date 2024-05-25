import os

def crear_fifo(path_fifo):
    if not os.path.exists(path_fifo):
        os.mkfifo(path_fifo)

def main():
    path_fifo = "fifo/fifo_server"
    print("La fifo esta " + path_fifo)
    crear_fifo(path_fifo)

    # Abrimos pipe

    with open(path_fifo, 'r') as fifo:
        # Se debe pasar "'path'\npid"
        mensaje = fifo.read().split("$$")
        print(f'el mensaje recibido es: {str(mensaje)}')
        path = mensaje[0]
        pid = mensaje[1]
        
        with open(path, 'r') as file:
            crear_fifo("fifo/"+pid)
            print("He creado la fifo")
            
            path_fifo2 = "fifo/"+str(pid)
            with open(path_fifo2, 'w') as fifo2:
                fifo2.write(file.read())
                fifo2.flush()
                print("he escrito en la fifo")

                # Borrar el archivo de control--> cliente empieza a leer
                control_file = "fifo/control_" + pid+".txt"
                if os.path.exists(control_file):
                    os.remove(control_file)
                    print("He borrado el archivo de control")

    os.remove(path_fifo)
    # El fifo de respuesta lo cierra el cliente por ahora.

if __name__ == "__main__":
    main()  
