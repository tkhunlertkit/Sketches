run: prog
	./prog

prog: stack.o main.o
	gcc -o prog stack.o main.o

main.o: main.c stack.h
	gcc -c -Wall -pedantic main.c

stack.o: stack.c stack.h
	gcc -c -Wall -pedantic stack.c

clean:
	rm *.o prog