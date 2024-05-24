import sys
import socket as s 
#Servidor

def leer_archivo(ruta_archivo):
    contenido_archivo = '' 
    with open(ruta_archivo, 'r') as file:
            contenido_archivo = file.read()
    return contenido_archivo

def leer_mensajes(socket):
    mensaje_completo = ''
    while True:
        mensaje, dir_cliente = socket.recvfrom(1024)
        #if not mensaje:
        if mensaje.decode('utf-8') == '$$$': #Ya se que no es un buen delimitador estoy probando que funcione
            break
        mensaje_completo += str(mensaje.decode('utf-8'))
    return (mensaje_completo, dir_cliente)

def enviar_mensajes(contenido_a_enviar, socket, direccion):
    bloque_mensaje = [contenido_a_enviar[i:i+1024] for i in range(0, len(contenido_a_enviar), 1024)]

    for bloque in bloque_mensaje:
        socket.sendto(bloque.encode('utf-8'), direccion)
    
    socket.sendto('$$$'.encode('utf-8'), direccion)
    return True

def main():
    socket_servidor = s.socket(s.AF_INET,s.SOCK_DGRAM)
    socket_servidor.bind(('127.0.0.1', 1025))

    ruta_archivo, dir_cliente = leer_mensajes(socket_servidor)
    sys.stdout.write('Se ha recibido la ruta\n')
    sys.stdout.flush()
    
    contenido_archivo = leer_archivo(ruta_archivo)
    enviar_mensajes(contenido_archivo, socket_servidor, dir_cliente)
    
    socket_servidor.close()

if __name__ == '__main__':
    main()
