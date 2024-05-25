import datetime

fecha_hora_actual = datetime.datetime.now()

cadena_fecha_hora = fecha_hora_actual.strftime("%Y-%m-%dT%H:%M:%S%z")

print(cadena_fecha_hora + "\n")
