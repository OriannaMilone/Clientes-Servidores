#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/un.h>
#include <unistd.h>

#define SOCKET "/tmp/socket"

void main(){
	struct sockaddr_un servidor_addr;
	char contenido[1024];
	int fd_s;

	fd_s = socket(AF_UNIX, SOCK_STREAM, 0);

	if(fd_s == -1){
		perror("Error al crear el socket");
		exit(EXIT_FAILURE);
	}
	
	// Aquí estamos configurando la dirección del servidor
	servidor_addr.sun_family = AF_UNIX; // Inficamos su Address Format
	strcpy(servidor_addr.sun_path, SOCKET); // Aquí estamos indicando que formato va a tener el socket
	//strncpy() <- 	Investigar
	if (connect(fd_s, (struct sockaddr *) &servidor_addr, sizeof(servidor_addr)) == -1) { //sustituir el sizeof por el tipo
		perror("connect");
		exit(1);
	}
	
	char *mensaje = "Pasame la hora!";

	if (send(fd_s, mensaje, strlen(mensaje)+1, 0) < 0) { // Este +1 es por el terminador
		perror("send");
		exit(1);
	}
	
	int bytes_leidos = recv(fd_s, contenido, sizeof(contenido), 0);
	if (bytes_leidos == -1) {
		perror("recv");
		exit(1);
	}

	contenido[bytes_leidos] = '\0';
	write(1, contenido, bytes_leidos);
	write(1, "\n", strlen("\n"));

	close(fd_s);
}
