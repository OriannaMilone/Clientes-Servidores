import os
import sys
import time

def main():
    path_fifo = "fifo/fifo_server"
    pid = os.getpid()
    print(f'mi PID es {str(pid)}')
   # path_fifo = input("Indique el path de la fifo: ")
    
    mensaje = input("Indique el mensaje que quiera enviar: ")
    mensaje_final = mensaje + "$$" + str(pid)

    with open(path_fifo, 'w') as fifo:
        fifo.write(mensaje_final)
    
#  ar al servidor
#    control_file = "fifo/control_" + str(pid)+".txt"
#    with open(control_file, 'w') as control:
#        control.write("esperando a que el servidor cree una fifo")
#
#    # Cuando el servidor lo borre --> seguimos
#    while os.path.exists(control_file):
#        print("Esperando al servidor...")
#        time.sleep(0.5)
#        

    with open("fifo/"+str(pid), 'r') as fifo:
        contenido = fifo.read()
        sys.stdout.write(contenido)
        sys.stdout.flush() 

if __name__ == "__main__":
    main()
