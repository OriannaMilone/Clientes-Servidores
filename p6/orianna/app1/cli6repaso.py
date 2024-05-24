#Código Cliente TCP
import socket as s
import sys 

def main():
    sock_cli = s.socket(AF_INET, SOCK_STREAM)
    sock_cli.connect(('0.0.0.0', 2222))

    archivo_a_leer = sys.argv[1]

    sys.stdout.write('Enviando la ruta del archivo al servidor: ' + archivo_a_leer)
    
    #enviarlo por partes? o solo enviarlo y leerlo  por partes
    sock_cli.send(archivo_a_leer)
    


    #Hacerlo en un buclecito
    sock_cli.recv()

    sock_cli.shutdown(SHUT_WR)

if __name__ == '__main__':
    main()
