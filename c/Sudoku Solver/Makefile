run: prog
	./prog $2

prog: main.o check.o 
	gcc -o prog main.o check.o

main.o: main.h main.c check.c global.h variable.h
	gcc -c -Wall -pedantic main.c

check.o: check.c check.h global.h variable.h
	gcc -c -Wall -pedantic check.c

clean:
	rm *.o prog *~