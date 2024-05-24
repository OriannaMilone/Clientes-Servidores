#Código Clientes 
import socket as s
import sys

def main():
    if len(sys.argv) != 3:
        puerto_socket = 1029
        ip_socket = '0.0.0.0'
        print(f"Usando los valores por defecto\nIP:{ip_socket}\nPuerto:{puerto_socket}")
    else:
        ip_socket = sys.argv[1] #Lo puedo parsear con un XR
        puerto_socket = int(sys.argv[2]) #Gestionar luego las excepciones

    print(f"Parametros en uso\nIP:{ip_socket}\nPuerto:{puerto_socket}")
    direccion_socket = (ip_socket, puerto_socket)

    socket_cliente = s.socket(s.AF_INET, s.SOCK_STREAM)
    socket_cliente.connect(direccion_socket)
    
    while True:
        mensajes_recibidos = socket_cliente.recv(4096).decode('utf-8')
        if mensajes_recibidos:
            print(mensajes_recibidos)

        mensaje = input('> ')
        socket_cliente.send(mensaje.encode('utf-8'))

        if mensaje.lower() == 'exit':
            print("Saliendo del chat...")
            break

    socket_cliente.close() 

if __name__ == '__main__':
    main()
