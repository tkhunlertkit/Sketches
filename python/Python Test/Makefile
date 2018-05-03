run: prog
	./prog

prog: quicksort.o
	gcc -o prog quicksort.o

quicksort.o: quicksort.c
	gcc -c -Wall -pedantic quicksort.c
