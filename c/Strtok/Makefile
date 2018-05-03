run: clean prog
	./prog

prog: main.o
	gcc -o prog main.o

main.o: main.c
	gcc -Wall -pedantic -c main.c

clean:
	-rm -rf main.o prog