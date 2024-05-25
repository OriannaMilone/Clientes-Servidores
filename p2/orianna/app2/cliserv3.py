import os 
import sys 
import datetime

def main():

    tub_cli = os.pipe()
    tub_serv = os.pipe()

    if(os.fork() == 0): #Servidor (hijo)
        os.close(tub_cli[1])
        os.close(tub_serv[0])
        
        sys.stdout.write('Soy el servidor con pid(' + str(os.getpid())+ ') y enviaré la hora a mi padre con pid('+ str(os.getppid())+ ')\n')
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        os.write(tub_serv[1], fecha_actual.encode('utf-8'))
    else: 
        os.close(tub_cli[0])
        os.close(tub_serv[1])
        
        fecha_recibida = os.read(tub_serv[0], 4096)
        sys.stdout.write('Soy el cliente con pid(' + str(os.getpid())+ ')\n')
        sys.stdout.write('Fecha recibida por el servidor: ' + str(fecha_recibida.decode('utf-8'))+ '\n')



if __name__ == '__main__':
    main()
