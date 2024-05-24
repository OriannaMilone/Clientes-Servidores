import socket
import sys
import ast
import select

def cerrar_clientes(conexiones):
    for cliente in conexiones:
        cliente.send(("$exit$").encode())

def enviar_mensaje_a_todos(mensaje, conexiones):
    for cliente in conexiones:
        cliente.send(mensaje.encode())
        # deberiamos poner unos try

def recibir_mensaje_cliente(socket):
    data = socket.recv(1024) 
    # data debería ser:"nick: mensajeconexiones
    print("He recibido " + str(data.decode()))
    return data

    
def main():

    direcc_socket = sys.argv[1]
    puerto = int(sys.argv[2])
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((direcc_socket, puerto))
    servidor.listen(5)

    print("Servidor Iniciado en el puerto 8088 " + "\U0001F600")

    conexiones_clientes = [servidor]
    clientes = {}
    
    try:
        while True:
            ready_rlist, ready_wlist, ready_xlist = select.select(conexiones_clientes,[], [])

            for s in ready_rlist:
                if s == servidor:
                    conexion, direccion = servidor.accept()
                    print(f'Nueva conexion desde {direccion}')
                    clientes[conexion] = direccion
                    conexiones_clientes.append(conexion)
                    
                else:
                    data = recibir_mensaje_cliente(s)

                    if data:
                        mensaje = data.decode()
                        enviar_mensaje_a_todos(mensaje, clientes)

                    else:
                        #no hay datos = cliente cerró conexión
                        sys.stderr.write(f'Cliente {clientes[s]} se ha desconectado\n')
                        s.close()
                        conexiones_clientes.remove(s)
                        del clientes[s]
                    

    finally:
        print("Cerrando el servidor...")
        servidor.close()
        cerrar_clientes(clientes)
        

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.stderr.write("Uso: python serv7Select.py <dirección_socket> <puerto>\n")
        sys.stderr.write("Ejemplo: python serv7Select.py 127.0.0.1 8088\n")

        sys.exit(1)
    main()
