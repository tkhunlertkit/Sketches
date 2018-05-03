#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "Collection.h"
#include "./Stack/stack.h"

static const int SIZE = 15;
static const int kth = 5;

void my_print(void *data, char **result) {
	*result = (char*) malloc(sizeof(int));
	sprintf(*result, "%d", *(int*)data);
	return;
}

int compare(void *item1, void *item2) {
	int ret = *(int*)item1 - *(int*)item2;
	return ret;
}

int main(int argc, char** argv) {

	Collection *my_collection = (Collection*) malloc(sizeof(Collection));
	char *result;
	int *removed;
	void *t;
	int x;
	int i;
	srand(time(NULL));

	initialize(&my_collection, sizeof(int));

	// printf("\n------ Begin Program ------\n");
	// printf("\nStart Collection\n%s\n", result);
	for (i=0; i<SIZE; ++i) {
		x = rand()%100;
		// printf("adding: %d\n", x);
		if (add(&my_collection, &x, compare) == 0) {
			// printf("%d is a duplicate in the list\n", x);
		}
	}

	result = to_string(my_collection, my_print);
	printf("\n%s\n", result);
	printf("The size of collection is: %zd\n", my_collection->tree_size);
	create_dot_file(my_collection, "Graph_Before_Remove.dot", my_print);
	// printf("what to remove?: ");
	// scanf("%d", &i);

	x = rand()%my_collection->tree_size + 1;
	printf("x: %d\n", x);
	i = *(int*)get_kth_smallest(my_collection, x);
	printf("removing: %d\n", i);
	removed = (int*) remove_data(&my_collection, &i, compare);
	if (removed != NULL) {
		printf("Removed %d from colleciton returns: %d\n", i, *removed);
	}
	

	create_dot_file(my_collection, "Graph_After_Remove.dot", my_print);
	printf("The size of collection after removed is: %zd\n", my_collection->tree_size);
	load_balancing(&my_collection, compare);
	
	printf("\nAfter reordered, The size of collection is: %zd\n", my_collection->tree_size);
	result = to_string(my_collection, my_print);
	printf("\n%s\n", result);
	create_dot_file(my_collection, "Graph.dot", my_print);
	printf("dot files completed\n");
	t = get_kth_smallest(my_collection, kth);
	if (t != NULL)
		printf("retruned from get_kth_node: %d\n", *(int*)t);
	else
		printf("t is null");
	free_collection(&my_collection);
	// printf("\nAfter Free");
	result = to_string(my_collection, my_print);
	printf("\n%s\n", result);
	return 0;
}