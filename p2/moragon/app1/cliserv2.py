import os, sys, io

def main():

    rd1, wd1 = os.pipe() # cliente-servidor
    rd2, wd2 = os.pipe() # servidor-cliente
    
    r1, w1 = os.fdopen(rd1, 'rb'), os.fdopen(wd1, 'wb') # cliente-servidor
    r2, w2 = os.fdopen(rd2, 'rb'), os.fdopen(wd2, 'wb') # servidor-cliente
        
    if os.fork(): # Entra el padre
    
        if os.fork(): # Entra padre
            r1.close()
            w1.close()
            r2.close()
            w2.close()
            # Experamos que terminen los hijos
            os.wait()
            os.wait()
    
        else: # Entra el cli2
            r1.close()
            w2.close()
    
            #w1.write(b'fichero.txt')
            #w1.write(b'/etc/services')
            w1.write(b'/bin/sh')
            w1.close()
    
            datos_bin = r2.read() # <- Se queda aquí parado
            try:
                sys.stdout.write(datos_bin.decode('utf-8'))
            except UnicodeDecodeError:
                #print(datos_bin)
                sys.stdout = sys.stdout.detach()
                sys.stdout.write(datos_bin)
            #w1.close()

    else: # Entra serv2
        w1.close()
        r2.close()

        path = r1.read()#.decode()

        with open(path, 'rb') as file:
            content = file.read()

        w2.write(content)
        w2.close()


    sys.exit(0)
    

if __name__ == '__main__':
    main()

