import socket
from datetime import datetime
import hashlib
import select

class Servidor:
    def __init__(self, puerto):
        self.puerto = puerto
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.codificacion = 'utf-8'
        self.formato_hora = "%H:%M:%S"
        
        self.s.bind(('0.0.0.0', puerto))
        self.s.listen()

        self.sockets = [self.s]
        self.grupo_user = {}
        self.grupos = {"all" : set()}
        self.archivo_credenciales = "credenciales.csv"

    def obtener_hora(self):
        hora = datetime.now().time()
        str_hora = hora.strftime(self.formato_hora)
        return str_hora
    
    def leer_mensaje(self, socket):
        '''
        mensaje = ""
        while True:
            info = socket.recv(1024)
            mensaje += info.decode(self.codificacion)
            if not info:
                break
        '''
        mensaje = socket.recv(1024).decode(self.codificacion)
        return mensaje

    def get_grupo(self, user):
        if user not in self.grupo_user:
            self.grupo_user[user] = 'all'
            self.grupos["all"].append(user)
        
        return self.grupo_user[user] 
    
    def encriptar(self, datos):
        return hashlib.sha256(datos.encode(self.codificacion)).hexdigest()

    def comprobar_credenciales(self, usuario, passwd):
        pas_enc = self.encriptar(passwd)

        registro = f'"{usuario}"' + ', ' + pas_enc
        print("registro: " + registro + "\n")
        with open(self.archivo_credenciales, 'r') as fd:
            contenido = fd.read()

        return registro in contenido

    def tratar_mensaje(self, mensaje):
        usuario, contenido = mensaje.split("@@")
        grupo = self.get_grupo(usuario)
            
        nuevo_mensaje = "\nHora: " + self.obtener_hora() + "\n< " + usuario + " >  " + contenido
        print(f">><< {len(self.grupos.keys())}")
        for integrante in self.grupos[grupo]:
            #if usuario is not integrante:
            integrante.sendall(nuevo_mensaje.encode(self.codificacion))
            #integrante.flush()
        return True

        '''
        if mensaje == "": # Salir
            #print("EXIT\n")
            return False # Quitar conn

        elif "++" in mensaje: # Añadirte a un grupo
            #usuario, grupo = mensaje.split("++")
            #if grupo not in self.grupos:
            #    self.grupos[grupo] = []

            #self.grupos[grupo].append(usuario)
            #print("grupo\n")
            return None
        
        elif "||" in mensaje: # Comprobar credenciales
            usuario, passwd = mensaje.split("||")
            #print(f"credenciales: {self.comprobar_credenciales(usuario, passwd)}\n", flush=True)
            return self.comprobar_credenciales(usuario, passwd)

        else: # Mensajes ordinarios
        
            #print(f"mensaje: {mensaje}\n")
            usuario, contenido = mensaje.split("@@")
            grupo = self.get_grupo(usuario)
            
            nuevo_mensaje = "\nHora: " + self.obtener_hora() + "\n< " + usuario + " >  " + contenido
            print(f">><< {len(self.grupos.keys())}")
            #print(f"mensaje: {nuevo_mensaje}\n")
            for integrante in self.grupos[grupo]:
                #if usuario is not integrante:
                integrante.sendall(nuevo_mensaje.encode(self.codificacion))
                #integrante.flush()

            return True
        '''

    def main(self):
        while True:
            sockets_listos, _, _ = select.select(self.sockets.copy(), [], [])
            
            listo = sockets_listos[0]

            if listo == self.s:
                conn, addr = self.s.accept()
                self.sockets.append(conn)
                self.grupos['all'].append(conn)
            else:
                mensaje = self.leer_mensaje(listo)
            
                if not self.tratar_mensaje(mensaje):
                    listo.shutdown(socket.SHUT_RD)
                    self.sockets.remove(listo)

            
        
if __name__ == '__main__':
    Servidor(8080).main()

