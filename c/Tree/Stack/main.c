#include <stdio.h>
#include <stdlib.h>
#include "stack.h"

int main(int argc, char **argv) {
	int data[5], i, x;
	Stack *s = (Stack*) malloc(sizeof(Stack));

	for (i=0; i<5; ++i) {
		data[i] = (i + 1) * 2;
	}

	initialize_stack(&s);
	push(&s, &data[2], sizeof(&data[2]));
	printf("going into push\n");
	push(&s, &data[1], sizeof(&data[1
		]));
	printf("going into push\n");

	x = *(int*) peek(s);
	printf("peek return: %d\n", x);
	x = *(int*) pop(&s);
	printf("pop return: %d\n", x);
	x = *(int*) pop(&s);
	printf("pop return: %d\n", x);

	return 0;
}
