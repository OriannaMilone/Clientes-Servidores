import os
import pytz
import datetime

def calcular_fechaHora():
    zona_horaria_local = pytz.timezone(pytz.country_timezones['ES'][0])

    fecha_hora_local = datetime.datetime.now(tz=zona_horaria_local)
    fecha_hora_formateada = fecha_hora_local.strftime('%Y-%m-%dT%H:%M:%S%z')
    return fecha_hora_formateada

def cliente_servidor():
    
    r, w = os.pipe()
    rd, wd = os.pipe()

    pid = os.fork()

    if pid == 0:  #  hijo (servidor)
        print("Soy el Hijo con PID " + str(os.getpid()))
       
        os.close(w)
        os.close(rd)

        # Obtener fecha y hora + escribirlo en el pipe
        fechaHora = calcular_fechaHora()
        os.write(wd, fechaHora.encode())
        print("Soy el Proceso con PID " + str(os.getpid())+ " y he enviado << "+str(fechaHora)+" >>")

        os.close(r)
        os.close(wd)

        os._exit(0)
    else:  #  padre (cliente)
        print("Soy el Padre con PID " + str(os.getpid()))

        os.close(r)
        os.close(wd)

        # Leer la respuesta del servidor
        respuesta = os.read(rd, 1024).decode()
        print("Soy el proceso con PID " + str(os.getpid()) + " y he recibido la respuesta del servidor (mi hijo): " + respuesta )

        os.close(w)
        os.close(rd)

        # Esperar a que el proceso hijo (servidor) termine
        _, status = os.waitpid(pid, 0)
        if os.WIFEXITED(status):
            print("El proceso hijo (servidor) con PID", pid, "terminó correctamente.")
        else:
            print("El proceso hijo (servidor) con PID", pid, "terminó con error.")

        os._exit(0)

if __name__ == "__main__":
    cliente_servidor()

