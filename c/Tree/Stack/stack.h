#include <stdlib.h>

typedef struct Node {
	void *ptr;
	struct Node *next;
} Node;

typedef struct Stack {
	struct Node *head;
} Stack;

void initialize_stack(Stack **s);

void push(Stack **stack, void *data, size_t size_data);

void *pop(Stack **stack);

void *peek(const Stack *stack);

int empty(const Stack *stack);
