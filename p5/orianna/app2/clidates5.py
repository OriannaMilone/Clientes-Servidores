import sys
import socket as s
#Cliente

def leer_mensajes(socket):
    mensaje_completo = ''
    while True:
        mensaje, dirreccion = socket.recvfrom(1024)
        if mensaje.decode('utf-8') == '$$$':
            # break
            return (mensaje_completo, dirreccion)
        mensaje_completo += str(mensaje.decode('utf-8'))
    #return (mensaje_completo, dirreccion)

def enviar_mensajes(contenido_a_enviar, socket, direccion):
    bloque_mensaje = [contenido_a_enviar[i:i+1024] for i in range(0, len(contenido_a_enviar), 1024)]

    for bloque in bloque_mensaje:
        socket.sendto(bloque.encode('utf-8'), direccion)
    
    socket.sendto('$$$'.encode('utf-8'), direccion)
    return True

def main():
    dir_socket_serv = '127.0.0.1'
    puerto_socket_serv = 1025

    socket_cliente = s.socket(s.AF_INET, s.SOCK_DGRAM)

    enviar_mensajes('Dime la hora!', socket_cliente, (dir_socket_serv, puerto_socket_serv))
    
    sys.stdout.write('Se ha enviado la peticion\n')
    sys.stdout.flush()
    respuesta_final, _ = leer_mensajes(socket_cliente)
    sys.stdout.write("Datos leídos del servidor:\n" + respuesta_final)
    socket_cliente.close()

if __name__ == '__main__':
    main()
