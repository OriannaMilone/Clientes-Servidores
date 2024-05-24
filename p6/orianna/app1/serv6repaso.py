#Codigo Servidor TCP
import socket as s

def main()
    sock_serv = s.socket(AF_INET, SOCK_STREAM)
    sock_serv.bind(('0.0.0.0', 2222))

    sock_serv.listen()
    
    while True:
        sock_cli, dir_cli = sock_serv.accept()


if __name__ == '__main__':
    main()
