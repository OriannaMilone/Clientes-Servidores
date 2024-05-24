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


def crear_grupo_privado(conexion,data, grupos):
    # data --> paloma: $$grupo: 123:
    partes = data.split(": $$grupo ")
    nombre_grupo=partes[1]
    grupos[conexion] = nombre_grupo
    return grupos


def enviar_mensaje_a_cliente(conexion, mensaje):
    try:
        conexion.send(mensaje.encode())
        return True
    except Exception as e:
        sys.stderr.write("Error:", e)
        return False


def enviar_mensaje_al_grupo(mensaje, conexion, grupos):
    try:
        nickname = mensaje.split(':')[0]
        partes = mensaje.split('$$send')
        grupo, mensaje_user = partes[1].strip().split(' ',1)
        print(f'El grupo es {grupo} y el mensaje {mensaje_user}')

        clientes_grupo = {}
        for clave, val in grupos.items():
            if val == grupo:
                clientes_grupo[clave] = val
    
        mensaje_para_miembros = nickname + ": (grupo-"+grupo+") "+ mensaje_user
        enviar_mensaje_a_todos(mensaje_para_miembros, clientes_grupo)
        return True
    except Exception as e:
        sys.stderr.write("Error:", e)
        return False

def comandos_del_cliente(data, conexion, grupos={}):
    partes = data.split()

    if partes[1] == "$$grupo":
        if conexion in grupos:
            grupos = crear_grupo_privado(conexion, data, grupos)
            mensaje = "Se ha unido a un nuevo grupo " + str(grupos[conexion])
        else:
            grupos = crear_grupo_privado(conexion, data, grupos)
            mensaje = "Se ha unido al grupo " + str(grupos[conexion])
        return enviar_mensaje_a_cliente(conexion, mensaje)
    elif partes[1] == "$$send":
        return enviar_mensaje_al_grupo(data, conexion, grupos)
    else:
        return enviar_mensaje_a_cliente(conexion, "comando no válido")


def main():

    direcc_socket = sys.argv[1]
    puerto = int(sys.argv[2])
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((direcc_socket, puerto))
    servidor.listen(5)

    print("Servidor Iniciado en el puerto 8088 " + "\U0001F600")

    conexiones_clientes = [servidor]
    clientes = {}
    grupos = {}

    try:
        while True:
            ready_rlist, ready_wlist, ready_xlist = select.select(conexiones_clientes,[], [])

            for s in ready_rlist:
                if s == servidor:
                    conexion, direccion = servidor.accept()
                    print(f'Nueva conexion desde {direccion}')
                    clientes[conexion] = direccion
                    conexiones_clientes.append(conexion)
                    instrucciones = """
                    Bienvenido \U0001F600
                    Comandos importantes: 
                    - Crear un grupo -->  debes escribir $$grupo nombre_del_grupo (solo puedes estar en un grupo)
                    """
                    enviar_mensaje_a_cliente(conexion, instrucciones)
                    
                else:
                    data = recibir_mensaje_cliente(s)
                    
                    if data:
                        mensaje = data.decode()
                        if "$$" in mensaje:
                            comandos_del_cliente(mensaje, conexion, grupos)
                        else:
                            enviar_mensaje_a_todos(mensaje, clientes)

                    else:
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
        sys.stderr.write("Ejemplo: python3 serv7.py 127.0.0.1 8088\n")

        sys.exit(1)

    global conexiones_clientes
    global clientes
    global grupos

    main()
