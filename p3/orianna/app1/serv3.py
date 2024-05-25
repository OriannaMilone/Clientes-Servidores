import os
import sys

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
        sys.stdout.write('Entra en el Loop\n')
        sys.stdout.flush()
       
        data_recibida = os.read(tub_fifo_serv, 4096)
        ruta_archivo = data_recibida.decode('utf-8')
       # os.close(tub_fifo_serv)

        if data_recibida:
         with open(ruta_archivo, 'r') as archivo:
            contenido_fichero = archivo.read()

         tub_fifo_cli = os.open('/tmp/fifo_cli', os.O_WRONLY)
         os.write(tub_fifo_cli, contenido_fichero.encode('utf-8'))
         os.close(tub_fifo_cli)
        else: 
            sys.stdout.write('Fin de la comunicación\n')
            sys.stdout.flush()
            break

if __name__ == '__main__':
    main()
