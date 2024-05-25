#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>

void main(){
	char path_fifo_serv[] = "/tmp/fifo_servidor";
	char path_fifo_cliente[20];
	char contenido[1024];
	int fifo, fifo_respuesta;
	size_t bytes_leidos;
	
	sprintf(path_fifo_cliente, "/tmp/%d", getpid());

	mkfifo(path_fifo_cliente, 0666);

	fifo = open(path_fifo_serv, O_WRONLY);
	
	if (fifo == -1){
		fprintf(stderr, "No está creado el fifo para el servidor.\n");
	}
	
	write(fifo, path_fifo_cliente, strlen(path_fifo_cliente));
	close(fifo);
	
	fifo_respuesta = open(path_fifo_cliente, O_RDONLY);
		

	bytes_leidos = read(fifo_respuesta, contenido, sizeof(contenido));

	write(1, contenido, bytes_leidos);
	close(fifo_respuesta);
	remove(path_fifo_cliente);
}
