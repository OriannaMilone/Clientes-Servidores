import socket, select, re, hashlib

lista_de_sockets = []
set_de_clientes = set()

def main():
    global lista_de_sockets
    global set_de_clientes
    
    # Clave: re, valor: Funcionalidad
    #opciones = {
    #        r'*|&|&|*': enviar_mensaje,
    #        r'exit': cerrar_conn
    #        }

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.bind(("0.0.0.0", 8080))

        s.listen()

        lista_de_sockets.append(s)
        #lista_de_sockets = [s]

        #set_de_clientes = set()
        
        while True:

            socket_lectura, _, _ = select.select(lista_de_sockets, [], [])

            socket_listo = socket_lectura[0]

            if socket_listo == s:
                socket_cliente, cliente_address = socket_listo.accept()
                
                # Autentificacion
                datos = socket_cliente.recv(1024)
                mensaje = datos.decode()
                usuario, password = mensaje.split("|&|&|")

                if autentificar_cliente(usuario, password):
                    lista_de_sockets.append(socket_cliente)
                    set_de_clientes.add(socket_cliente)
                else:
                    socket_cliente.send(("servidor|&|&|CREDENCIALES INCORRECTAS").encode())
                    socket_cliente.close()



            else:
                datos = socket_listo.recv(1024)
                mensaje = datos.decode()

                # Clave: re, valor: Funcionalidad
                opciones = {
                    r'*|\&|\&|*': enviar_mensaje(datos, socket_cliente, socket_listo),
                    r'exit': cerrar_conn(socket_listo),
                    r'*': 
                        enviar_mensaje(("servidor|&|&|No existe ese comando").encode(), socket_cliente, socket_listo)
                    }

                if datos:
                    opciones[mensaje]
                    #for socket_cliente in set_de_clientes:
                        #if socket_cliente != socket_listo:
                            #socket_cliente.sendall(datos)
                    
                else:
                    cerrar_conn(socket_listo)
                    #if socket_listo in lista_de_sockets:
                        #lista_de_sockets.remove(socket_listo)

                    #if socket_listo in set_de_clientes:
                        #set_de_clientes.remove(socket_listo)

                    #socket_listo.close()

# Funcionalidad de envio de mensajes

def enviar_mensaje(mensaje, socket_cliente, socket_listo):
    global set_de_clientes

    for socket_cliente in set_de_clientes:
        if socket_cliente != socket_listo:
            socket_cliente.sendall(datos)

def cerrar_conn(socket_listo):
    global lista_de_sockets
    global set_de_clientes

    if socket_listo in lista_de_sockets:
        lista_de_sockets.remove(socket_listo)

    if socket_listo in set_de_clientes:
        set_de_clientes.remove(socket_listo)

    socket_listo.close()
    


# Funcionalidad para tratamiento de credenciales

def encriptar_contrasenna(contrasenna):
    return hashlib.sha256(contrasenna.encode()).hexdigest()

def guardar_credenciales(nombre, contrasenna) -> bool:
    fichero = "credenciales.csv"
    contrasenna_encrip = encriptar_contrasenna(contrasenna)
    with open(fichero, 'a') as f:
        salida = f.write("\"" + nombre + "\", " + contrasenna_encrip + "\n")

        return salida == 1 # Se ha ejecutado correctamente

def borrar_credenciales(nombre):
    fichero = "credenciales.csv"
    with open(fichero, 'r') as f:
        lineas = f.readlines()

    with open(fichero, 'w') as f:
        for linea in lineas:
            if ("\"" + nombre + "\"") not in linea:
                f.write(linea)

def autentificar_cliente(nombre, contrasenna):
    fichero = "credenciales.csv"
    
    contrasenna_encrip = encriptar_contrasenna(contrasenna)
    print("\"" + nombre + "\", " + contrasenna_encrip + "\n" )

    with open(fichero, 'r') as f:
        if ("\"" + nombre + "\", " + contrasenna_encrip + "\n" ) in f.readlines():
            return True

    return False



if __name__ == "__main__":
    main()
