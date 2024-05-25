import os
import sys 

def cliente_servidor():
    
    rd1, wd1 = os.pipe() # Tuberia cliente --> serv
    rd2, wd2 = os.pipe() # tuberia serv --> cliente

    r1, w1 = os.fdopen(rd1, 'rb'), os.fdopen(wd1, 'wb')  # cliente-servidor
    r2, w2 = os.fdopen(rd2, 'rb'), os.fdopen(wd2, 'wb')  # servidor-cliente
    pid = os.fork()

    if pid == 0:  #  hijo (servidor)

        w1.close() #os.close(w1)
        r2.close() #os.close(r2)

        path = r1.read().decode()
        print("Serv: he leido archivo del primer pipe")

        #### segunda pipe  ###

        with open(path, 'rb') as file:
            content = file.read()
        
        print("Serv: he leido el contenido del path")
        w2.write(content) #os.write(w2, contenido)
        
        print("Serv: he escrito en el pipe2")

        w2.close()
        sys.exit(0)
    else:  #  padre (cliente)
       
        r1.close() # os.close(r1)
        w2.close() # os.close(w2)

        path_archivo ="/var/log/dpkg.log"
        w1.write(path_archivo.encode())  # os.write(w1, path_archivo.encode())
        w1.close()
        print("Cliente: he escrito el archivo en el pipe")

        ####### segunda pipe ######
        
        contenido = r2.read()
        print("Cliente: he leido archivo del segundo pipe")
        sys.stdout.write(contenido.decode())

        r2.close() # os.close(r2)

        sys.exit(0)
        
if __name__ == "__main__":
    cliente_servidor()


