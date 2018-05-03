#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/uio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

void error(char *msg) 
{
	perror(msg);
	exit(0);
}

int main(int argc, char *argv[]) 
{
	int sockfd, newsockfd, portno;
	const int true = 1;
	socklen_t clilen;
	char buffer[256];
	struct sockaddr_in serv_addr, cli_addr;
	int n;
	int ws, ws_val;
	socklen_t ws_len, opt_len;
	

	ws_len = sizeof(ws_val);
	opt_len = sizeof(true);
	if (argc < 2) 
	{
		fprintf(stderr, "ERROR, no port provided\n");
		exit(0);
	}
	sockfd = socket(AF_INET, SOCK_STREAM, 0);
	if (sockfd < 0) 
		error("ERROR Opening socket");
	bzero((char *) &serv_addr, sizeof(serv_addr));
	portno = atoi(argv[1]);
	serv_addr.sin_family = AF_INET;
	serv_addr.sin_port = htons(portno);
	serv_addr.sin_addr.s_addr = INADDR_ANY;
	if (bind(sockfd, (struct sockaddr*) &serv_addr, sizeof(serv_addr)) < 0)
		error("ERROR on binding");
	listen(sockfd, 5);
	clilen = sizeof(cli_addr);

	/* Start Modified code */
	if (getsockopt(sockfd, SOL_SOCKET, SO_RCVBUF, (void *)&ws_val, &ws_len) < 0)
		error("ERROR Getting TCP Window size");
	printf("Receiving Window size Before configuration: %d\n", ws_val);
	ws = 1;
	if (setsockopt(sockfd, SOL_SOCKET, SO_RCVBUF, (char *)&ws, sizeof(ws)) < 0)
		error("ERROR Setting TCP Window size");

	if (getsockopt(sockfd, SOL_SOCKET, SO_RCVBUF, (void *)&ws_val, &ws_len) < 0)
		error("ERROR Getting TCP Window size");
	printf("Receiving Window size After configuration: %d\n", ws_val);
	/* End Modified Code */

	printf("Port opened, Waiting to accept connection from client\n");
	newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, &clilen);
	printf("client connected\n");
	printf("Listening...\n");
	if (newsockfd < 0)
		error("ERROR on accept");
	bzero(buffer, 256);
	n = read(newsockfd, buffer, 255);
	if (n < 0)
		error("ERROR Reading from socket");
	printf("Here is the message: %s", buffer);
	printf("Sending acknowledgement back\n");
	n = write(newsockfd, "I got your message", 18);
	if (n < 0) 
		error("ERROR Write to socket");
	printf("Waiting for client to close socket\n");
	sleep(1);
	shutdown(sockfd, 2);
	shutdown(newsockfd, 2);
	close(sockfd);
	close(newsockfd);
	return 0;

}