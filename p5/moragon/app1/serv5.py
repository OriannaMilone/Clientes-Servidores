import os, time, socket, struct

def leerfichero(path_fichero):
    with open(path_fichero, 'rb') as file:
        return file.read()

def main(): # IMPLEMENTAR UN ACK PARA ENVIAR EL SIGUIENTE DATAGRAMA
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0) as s:
        s.bind(("0.0.0.0", 8081))
        
        while True:
            path, addr = s.recvfrom(1024)
            contenido = leerfichero(path.decode())

            fragmentos = [contenido[i:i+1024] for i in range(0, len(contenido), 1024)]
            
            for fragmento in fragmentos:
                # Le añadimos una cabecera
                cabecera = struct.pack('!I', len(fragmento))

                mensaje = cabecera + fragmento

                s.sendto(mensaje, addr)

            # Para marcar el final de los fragmanetos
            s.sendto(struct.pack('!I', 0), addr) 
            
if __name__ == '__main__':
    main()
