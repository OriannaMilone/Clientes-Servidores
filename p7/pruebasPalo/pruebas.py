mensaje = "jose: $$send grupo_ejemplo Hola, ¿cómo están?"

# Dividir el mensaje en partes utilizando el delimitador ':'
parts = mensaje.split(':')

# El nickname estará en la primera parte
nickname = parts[0].strip()

# La segunda parte contiene el comando, el nombre del grupo y el mensaje
# Dividir esta parte en partes usando el delimitador ' '
command_and_group, message = parts[1].strip().split(' ', 1)

# El comando, el nombre del grupo y el mensaje estarán separados por ' '.
# Dividir esta parte en partes utilizando el delimitador ' '
command, group = command_and_group.split(' ', 1)

print("Nickname:", nickname)
print("Grupo:", group)
print("Mensaje:", message)

