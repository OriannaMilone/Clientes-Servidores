import os, sys, datetime, time

def calcular_fecha():
    fecha_hora_actual = datetime.datetime.now()

    cadena_fecha_hora = fecha_hora_actual.strftime("%Y-%m-%dT%H:%M:%S%z")

    return cadena_fecha_hora

def main():

    rd1, wd1 = os.pipe() # cliente-servidor

    r1, w1 = os.fdopen(rd1, 'r'), os.fdopen(wd1, 'w') # cliente-servidor

    if os.fork(): # Entra el padre

        if os.fork(): # Entra padre
            r1.close()
            w1.close()
            # Experamos que terminen los hijos
            os.wait()
            os.wait()
            sys.exit(0)
    
        else: # Entra el serv2
            r1.close()
            while True: 
                w1.write(calcular_fecha() + "\n")
                w1.flush()
            w1.close()
    else: # Entra cli2
        w1.close()
        while True:
            print(r1.readline())
        r1.close()
        

if __name__ == "__main__":
    main()
