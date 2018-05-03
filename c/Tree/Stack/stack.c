#include "stack.h"
#include <stdlib.h>

void initialize_stack(Stack **s) {
	(*s)->head = (Node*) malloc(sizeof(Node));
	(*s)->head = NULL;
}

void push(Stack **stack, void *data, size_t size_data) {
	Node *t = malloc(sizeof(Node));
	t->ptr = malloc(size_data);
	t->ptr = data;
	t->next = (*stack)->head;
	(*stack)->head = t;
}

void *pop(Stack **stack) {
	void *ret;
	Node *head;
	if (empty((*stack)) == 0) {
		ret = (*stack)->head->ptr;
		free((*stack)->head);
		head = (*stack)->head;
		(*stack)->head = head->next;
		return ret;
	}
	else {
		return NULL;
	}
}

void *peek(const Stack *stack) {
	if (empty(stack) == 0) {
		
		return stack->head->ptr;
	}
	else {
		return NULL;
	}
}

int empty(const Stack *stack) {
	return stack->head == NULL;
}
