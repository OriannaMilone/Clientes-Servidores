import os

def cliente_servidor():
    
    r, w = os.pipe()
    rd, wd = os.pipe()

    pid = os.fork()

    if pid == 0:  #  hijo (servidor)
        with open("diagnostico", "a") as diag_file:
            diag_file.write("Soy el Hijo con PID " + str(os.getpid()) + "\n")
       
        os.close(w)
        os.close(rd)

        path = os.read(r, 1024).decode()
        with open("diagnostico", "a") as diag_file:
            diag_file.write("Soy el Proceso con PID " + str(os.getpid()) + " y el path recibido es: << "+ path +" >>\n")

        with open(path, 'r') as f:
            contenido = f.read()
            os.write(wd, contenido.encode())
        with open("diagnostico", "a") as diag_file:
            diag_file.write("Soy el hijo, he leído el PATH del cliente y lo he devuelto\n")

        os.close(r)
        os.close(wd)

        os._exit(0)
    else:  #  padre (cliente)
        with open("diagnostico", "a") as diag_file:
            diag_file.write("Soy el Padre con PID " + str(os.getpid()) + "\n")

        os.close(r)
        os.close(wd)

        path_archivo ="archivo.txt"
        os.write(w, path_archivo.encode())
        with open("diagnostico", "a") as diag_file:
            diag_file.write("Soy el proceso con PID "+ str(os.getpid()) + " y he enviado el path << "+ path_archivo +" >>\n")

        respuesta = os.read(rd, 1024).decode()
        with open("diagnostico", "a") as diag_file:
            diag_file.write("Soy el proceso con PID " + str(os.getpid()) + " y he recibido la respuesta del servidor (mi hijo): " + respuesta + "\n")

        os.close(w)
        os.close(rd)

if __name__ == "__main__":
    cliente_servidor()

