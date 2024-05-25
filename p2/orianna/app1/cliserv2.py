import os
import sys

def main():
    tub_cli = os.pipe()
    tub_serv = os.pipe()
    
    if (os.fork()  == 0): #El hijo es el Servidor:
        os.close(tub_cli[1]) # Cerramos la escritura del cliente
        os.close(tub_serv[0]) # Cerramos la lectura del servidor
       
        sys.stdout.write('Proceso Servidor: ' + str(os.getpid()) + '\n')

        ruta_archivo = os.read(tub_cli[0], 4096)
        ruta_archivo = ruta_archivo.decode('utf-8').strip()
        ruta_archivo = os.path.expanduser(ruta_archivo)

        with open(ruta_archivo, 'r') as archivo:
            contenido_fichero = archivo.read()
    
        os.write(tub_serv[1], contenido_fichero.encode('utf-8'))
        os.close(tub_serv[1]) #Cerramos despues de escribir por buena práctica (si, no?)
    else: 
        os.close(tub_cli[0]) #Cerrar la lectura del cliente
        os.close(tub_serv[1]) # Cerramos la escritura del serv
        
        sys.stdout.write('Proceso Cliente: ' + str(os.getpid())+ '\n')

        os.write(tub_cli[1], '/home/ped2/p2/orianna/app1/archivo_prueba.txt'.encode('utf-8'))
        os.close(tub_cli[1])

        #Lectura de resultados:
        contenido_final_recibido = os.read(tub_serv[0], 4096)
        contenido_final_recibido = contenido_final_recibido.decode('utf-8').strip()

        sys.stdout.write('\nCliente ' + str(os.getpid()) +' ha recibido: ')
        sys.stdout.write(str(contenido_final_recibido))
        sys.stdout.flush()
        sys.stdout.write('\n')

if __name__ == '__main__':
    main()
