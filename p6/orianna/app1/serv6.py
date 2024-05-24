import sys
import socket as s 
#Servidor

def leer_archivo(ruta_archivo):
    contenido_archivo = '' 
    with open(ruta_archivo, 'r') as file:
            contenido_archivo = file.read()
    return contenido_archivo

def main():
    socket_servidor = s.socket(s.AF_INET,s.SOCK_STREAM)
    socket_servidor.bind(('0.0.0.0', 1026))
   
    #while True:
    socket_servidor.listen()
    sys.stdout.write('Escuchando\n')
    sys.stdout.flush()
        
    while True:
        socket_cliente, dir_cliente = socket_servidor.accept()
    
        ruta_archivo = socket_cliente.recv(4096) 
        sys.stdout.write('Se ha recibido la ruta\n')
        sys.stdout.flush()
    
        contenido_archivo = leer_archivo(ruta_archivo.decode('utf-8'))
        socket_cliente.send(contenido_archivo.encode('utf-8'))
    
        socket_cliente.close()

    socket_servidor.close()

if __name__ == '__main__':
    main()
