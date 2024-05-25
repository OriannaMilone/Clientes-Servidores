import os
import sys

#Cliente

def main():
    #tub_fifo_serv = '/tmp/fifo_serv'

    if not os.path.exists('/tmp/fifo_cli'):
        tub_fifo_cli = os.mkfifo('/tmp/fifo_cli')
        sys.stdout.write('Se ha creado con exito la tubería del cliente\n')
        sys.stdout.flush()

    tub_fifo_serv = os.open('/tmp/fifo_serv', os.O_WRONLY)
    sys.stdout.write('Se ha abierto la tuberia del Servidor\n')
    sys.stdout.flush()
    os.write(tub_fifo_serv, '/home/ped2/p3/orianna/app1/archivo_prueba.txt'.encode('utf-8'))
    sys.stdout.write('Se ha escrito en  la tuberia del Servidor\n')
    sys.stdout.flush()
    os.close(tub_fifo_serv)

    tub_fifo_cli = os.open('/tmp/fifo_cli', os.O_RDONLY)
    sys.stdout.write('Se ha abierto la tuberia del cliente\n')
    sys.stdout.flush()
    
    data_recibida = os.read(tub_fifo_cli, 4096)
    sys.stdout.write("Datos leídos de la FIFO:\n" + str(data_recibida.decode('utf-8')))
    os.close(tub_fifo_cli)

if __name__ == '__main__':
    main()
