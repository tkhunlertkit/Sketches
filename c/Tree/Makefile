run: prog
	./prog
	dot Graph.dot -Tsvg > graph.svg
	dot Graph_Before_Remove.dot -Tsvg > Graph_Before_Remove.svg
	

prog: main.o Collection.o stack.o
	gcc -g -o prog main.o Collection.o

main.o: main.c Collection.h ./Stack/stack.h
	gcc -g -c -Wall -padentic main.c

Collection.o: Collection.c Collection.h
	gcc -g -c -Wall -pedantic Collection.c

stack.o: ./Stack/stack.h ./Stack/stack.c
	gcc -g -c -Wall -pedantic ./Stack/stack.c

clear:
	rm prog *.o

dot: Graph.dot Graph_Before_Remove.dot
	dot Graph.dot -Tsvg > graph.svg
	dot Graph_After_Remove.dot -Tsvg > Graph_After_Remove.svg
	dot Graph_Before_Remove.dot -Tsvg > Graph_Before_Remove.svg