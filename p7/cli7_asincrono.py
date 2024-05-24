import socket
import asyncio

async def recv_from(reader):
    while True:
        print("aaaaaaaaaaaaaaaaaaaa", flush = True)
        datos = await reader.read(1024)
        if not datos:
            break

        datos_de = datos.decode()
        cliente, mensaje = datos_de.split("|&|&|")
        print(f"<<{cliente}>> {mensaje}")

async def main():
        reader, writer = await asyncio.open_connection("0.0.0.0", 8086)

        # Empezamos a escuchar:
        tarea_recv_from = asyncio.create_task(recv_from(reader))


        # Esperar a la entrada por terminal:
        
        writer.write(("annademe").encode())
        await writer.drain()

        while True:
            entrada = input("<<TU>> ")

            writer.write(("Carlos|&|&|" + entrada).encode())
            await writer.drain()

        writer.close()
        await writer.wait_closed()

        await tarea_recv_from

if __name__ == "__main__":
    asyncio.run(main())
