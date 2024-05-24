import sys
import socket as s 
import datetime
#Servidor

def leer_mensajes(socket):
    mensaje_completo = ''
    while True:
        mensaje, dir_cliente = socket.recvfrom(1024)
        #if not mensaje:
        if mensaje.decode('utf-8') == '$$$': #Ya se que no es un buen delimitador estoy probando que funcione
            break
        mensaje_completo += str(mensaje.decode('utf-8'))
    return (mensaje_completo, dir_cliente)

def enviar_mensajes(contenido_a_enviar,socket, direccion):
    bloque_mensaje = [contenido_a_enviar[i:i+1024] for i in range(0, len(contenido_a_enviar), 1024)]

    for bloque in bloque_mensaje:
        socket.sendto(bloque.encode('utf-8'), direccion)
    
    socket.sendto('$$$'.encode('utf-8'), direccion)
    return True

def main():
    socket_servidor = s.socket(s.AF_INET,s.SOCK_DGRAM)
    socket_servidor.bind(('127.0.0.1', 1025))

    while True:
        ruta_archivo, dir_cliente = leer_mensajes(socket_servidor)
    
        sys.stdout.write('Se ha recibido la petición\n')
        sys.stdout.flush()
    
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n")
        enviar_mensajes(fecha_actual, socket_servidor, dir_cliente)
    
    socket_servidor.close()

if __name__ == '__main__':
    main()
