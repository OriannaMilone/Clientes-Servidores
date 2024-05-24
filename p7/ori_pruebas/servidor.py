#Código Servidor
import select
import socket as s
import sys

def aprobar_usuarios(usuarios_pendientes, socket_serv):
    usuarios_conectados = []
    nombre_usuario = 'usuario_pruebas'
    for user in usuarios_pendientes:
        socket_cliente, direccion_cliente = user.accept()
        print("Nuevo usuario conectado:", direccion_cliente)
        usuarios_conectados.append(socket_cliente)
    return nombre_usuario, usuarios_conectados

def main():
    if len(sys.argv) != 4:
        puerto_socket = 1029
        ip_socket = '0.0.0.0'
        num_max_conexiones = 3
        print(f"Usando los valores por defecto\nIP:{ip_socket}\nPuerto:{puerto_socket}\nNumero máximo de conexiones:{num_max_conexiones}")
    else:
        ip_socket = sys.argv[1]
        puerto_socket = int(sys.argv[2])
        num_max_conexiones = int(sys.argv[3])

    print(f"Parametros en uso\nIP:{ip_socket}\nPuerto:{puerto_socket}\nNumero máximo de conexiones:{num_max_conexiones}")
    
    socket_serv = s.socket(s.AF_INET, s.SOCK_STREAM)
    direccion_socket = (ip_socket, puerto_socket)
    socket_serv.bind(direccion_socket)
    socket_serv.listen(num_max_conexiones)
    
    sys.stdout.write('Esperando usuarios\n')
    sys.stdout.flush()

    usuarios_esperando = [socket_serv]
    mensajes = []
  #      usuarios_pendientes, _, _ = select.select(usuarios_esperando, [], [])

    while True:
        usuarios_pendientes, _, _ = select.select(usuarios_esperando, [], [])
        
        nombre_usuario, usuarios_conectados = aprobar_usuarios(usuarios_pendientes, socket_serv)
        for usuario in usuarios_conectados:
            mensaje = usuario.recv(4096).decode('utf-8')
            if mensaje:
                mensajes.append((nombre_usuario, mensaje))

            for mensaje in mensajes:
                    usuario.send(str(mensaje).encode('utf-8'))

        mensajes = []

if __name__ == '__main__':
    main()

