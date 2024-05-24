import socket
import hashlib
import asyncio

clientes = set()

async def atender_cliente(reader, writer):
    global clientes
    
    try:
        while True:
            datos = await reader.read(1024)
            if not datos:
                break
            
            mensaje = datos.decode() 
            
            if mensaje == "annademe":
                clientes.add(writer)

            #if writer not in clientes:
            #    clientes.add(writer)
                #print("ANNADIDO 1")

            else:
                for cliente in clientes:
                    #print("MENSAJE")
                    if cliente != writer:
                        cliente.write(datos)
                        await cliente.drain()

    except asyncio.CancelledError:
        print(2, "Conexion de cliente cancelada")

    finally:
        if writer in clientes:
            clientes.remove(writer)
        writer.close()
        await writer.wait_closed()


async def main():
    servidor = await asyncio.start_server(atender_cliente, "0.0.0.0", 8086)
    async with servidor:
        await servidor.serve_forever()

# Funcionalidad para tratamiento de credenciales

def autentificar_cliente(nombre, contrasenna) -> bool:
    return False

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

    

if __name__ == '__main__':
    asyncio.run(main())
