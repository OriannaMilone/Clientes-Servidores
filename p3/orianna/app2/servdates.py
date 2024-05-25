import os
import sys
import datetime
#Servidor

def main():
    if not os.path.exists('/tmp/fifo_serv'):
        tub_fifo_serv = os.mkfifo('/tmp/fifo_serv')
        sys.stdout.write('Se ha creado con exito la tubería del servidor\n')
        sys.stdout.flush()
       
    tub_fifo_serv = os.open('/tmp/fifo_serv', os.O_RDONLY)
    sys.stdout.write('Abre tuberia del servidor\n')
    sys.stdout.flush()
   
    while True:
        peticion = os.read(tub_fifo_serv, 4096)
    
        if peticion:
            tub_fifo_cli = os.open('/tmp/fifo_cli', os.O_WRONLY)
            fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n")
            os.write(tub_fifo_cli,fecha_actual.encode('utf-8'))
            os.close(tub_fifo_cli)
        else: 
            sys.stdout.write('Fin de la comunicación\n')
            sys.stdout.flush()
            break

if __name__ == '__main__':
    main()
