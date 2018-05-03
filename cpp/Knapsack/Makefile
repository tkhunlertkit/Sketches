run: main
	./main

main: main.o Item.o KnapSack.o KnapSackDynamic.o
	g++ -o main main.o item.o KnapSack.o KnapSackDynamic.o

main.o: main.cpp Item.h KnapSack.h KnapSackDynamic.h
	g++ -pedantic -Wall -c main.cpp

Item.o: Item.cpp Item.h
	g++ -pedantic -Wall -c Item.cpp

KnapSack.o: KnapSack.cpp KnapSack.h Item.h
	g++ -pedantic -Wall -c KnapSack.cpp

KnapSackDynamic.o: KnapSack.h Item.h KnapSackDynamic.h KnapSackDynamic.cpp
	g++ -pedantic -Wall -c KnapSackDynamic.cpp

clean:
	rm *.o