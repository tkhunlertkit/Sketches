run_server: server client
	./server 53211 &
	./client localhost 53211 < test.txt

server: server.o
	gcc -o server server.o
server.o: server.c
	gcc -Wall -padentic -c server.c

client: client.o
	gcc -o client client.o

client.o: client.c
	gcc -Wall -pedantic -c client.c

clean: *.o
	rm *.o server client