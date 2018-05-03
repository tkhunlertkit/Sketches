run: prog
	./prog

prog: fork.o
	gcc -o prog fork.o

fork.o: fork.c
	gcc -c -Wall -pedantic fork.c