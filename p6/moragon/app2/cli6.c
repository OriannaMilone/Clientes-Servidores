#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <sys/types.h>
#include <arpa/inet.h>
#include <unistd.h>

#define IP "127.0.0.1"
#define PUERTO 8082
#define BUFFER_SIZE 1024

void main(){
	struct sockaddr_in servidor_addr;
	char contenido[BUFFER_SIZE];
	int fd_s;
	socklen_t servidor_addr_len = sizeof(servidor_addr);
	ssize_t recv_bytes;

	fd_s = socket(AF_INET, SOCK_STREAM, 0);

	if(fd_s == -1){
		perror("Error al crear el socket");
		exit(EXIT_FAILURE);
	}
	
	// Aquí estamos configurando la dirección del servidor
	
	memset(&servidor_addr, 0, sizeof(servidor_addr));

	servidor_addr.sin_family = AF_INET; // Inficamos su Address Format
	
	servidor_addr.sin_port = htons(PUERTO);
	
	if (inet_pton(AF_INET, IP, &servidor_addr.sin_addr) <= 0) {
		perror("inet_pton");
		exit(EXIT_FAILURE);
	}

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
