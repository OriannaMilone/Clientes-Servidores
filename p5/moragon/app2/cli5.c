#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <sys/types.h>
#include <arpa/inet.h> // Cambiamos la libreria
#include <unistd.h>

// Definimos las variables estaticas
#define IP "127.0.0.1"
#define PUERTO 8080
#define BUFFER_SIZE 1024

void main(){
	struct sockaddr_in servidor_addr;
	char contenido[BUFFER_SIZE];
	int fd_s;
	socklen_t servidor_addr_len = sizeof(servidor_addr);
	ssize_t recv_bytes;

	fd_s = socket(AF_INET, SOCK_DGRAM, 0);

	if(fd_s == -1){
		perror("Error al crear el socket");
		exit(EXIT_FAILURE);
	}
	
	// Aquí estamos configurando la dirección del servidor

	// Completamos un bloque de memoria con todo 0's, esto es para saber que tenemos valores conocidos en la dir. de memoria
	// Este bloque de memoria sera para el que tenga la direccion
	memset(&servidor_addr, 0, sizeof(servidor_addr));

	// Inficamos su Address Format
	servidor_addr.sin_family = AF_INET; 
	
	// Lo pasamos a little-endian
	servidor_addr.sin_port = htons(PUERTO);
	
	// Pasamos de str a formato binario <- gethostbyname
	if (inet_pton(AF_INET, IP, &servidor_addr.sin_addr) <= 0) {
		perror("inet_pton");
		exit(EXIT_FAILURE);
	}

	char *mensaje = "Pasame la hora!";

	if (sendto(fd_s, mensaje, strlen(mensaje), 0, (struct sockaddr *) &servidor_addr, sizeof(servidor_addr)) == -1) { // El 0 es para que no tenga flags
		perror("sendto");
		exit(EXIT_FAILURE);
	}
	
	int bytes_recibidos = recvfrom(fd_s, contenido, BUFFER_SIZE, 0, (struct sockaddr *) &servidor_addr, &servidor_addr_len); // El 0 es para que no tenga flags

	if (bytes_recibidos == -1) {
		perror("recvfrom");
		exit(EXIT_FAILURE);
	}

	contenido[bytes_recibidos] = '\0';
	write(1, contenido, bytes_recibidos);
	write(1, "\n", strlen("\n"));

	close(fd_s);
}
