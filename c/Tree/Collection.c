#include <string.h>
#include <stdlib.h>
#include "Collection.h"

#include <stdio.h>
#include "main.h"


void _print_children_to_file(const TreeNode *t, FILE *f, void (*my_print)(void *data, char **ret));

void _print_children(const TreeNode* t, char** result, void (*my_print)(void *data, char **ret));

void _free_node(TreeNode **t);

int _to_array(TreeNode *t, void ***array, int index, size_t size_of_element);

void _add_from_array(Collection **c, void **array, int min_index, int max_index, int (*compare)(void *item1, void *item2));

TreeNode *_get_kth_smallest(const TreeNode *t, int k);


void initialize(Collection** c, size_t data_size) {
	if ((*c)->root != NULL) {
		free_collection(c);
	}
	(*c)->root = NULL;
	(*c)->data_size = data_size;
	(*c)->tree_size = 0;
}

int add(Collection **c, void *data, int (*compare)(void *item1, void *item2)) {
	TreeNode* t = (TreeNode*)malloc(sizeof(TreeNode));
	t->data = malloc((*c)->data_size);
	memcpy(t->data, data, (*c)->data_size);
	t->left = NULL;
	t->right = NULL;
	t->size = 1;

	if (contains(*c, data, compare) == 1) {
		return 0;
	}
	if ((*c)->root == NULL) {
		(*c)->root = t;	
	}
	else {
		TreeNode* next = (*c)->root;
		TreeNode* parent = next;
		while(next) {
			parent = next;
			if (compare(data, next->data) < 0) { 
				next = next->left;
			}
			else {
				next = next->right;
			}
			parent->size++;
		}
		if (compare(data, parent->data) < 0) {
			parent->left = t;
		}
		else {
			parent->right = t;
		}
	}
	(*c)->tree_size++;
	return 1;
}

char* to_string(const Collection* c, void (*my_print)(void *data, char **ret)) {
	size_t size_of_element;
	char *result;
	if (c->tree_size == 0) {
		return NULL;
	}
	size_of_element = c->data_size;
	result = (char*) malloc(sizeof(size_of_element) * c->tree_size);
	strcat(result, "START -> ");
	_print_children(c->root, &result, my_print);
	strcat(result, "NULL");
	return result;
}

void _print_children(const TreeNode *t, char **result, void (*my_print)(void *data, char **ret)) {
	char *c;

	if (t == NULL) {
		return;
	}
	my_print(t->data, &c);
	strcat(c, " -> ");
	_print_children(t->left, result, my_print);
	strcat(*result, c);
	_print_children(t->right, result, my_print);
	return;
}

int contains(const Collection *c, void *data, int (*compare)(void *item1, void *item2)) {
	TreeNode* next = c->root;
	while (next) {
		if (compare(data, next->data) == 0) {
			return 1;
		}
		else if (compare(data, next->data) < 0) {
			next = next->left;
		}
		else {
			next = next->right;
		}
	}
	return 0;
}

void load_balancing(Collection **c, int (*compare)(void *item1, void *item2)) {
	Collection *new_collection = (Collection*) malloc(sizeof(Collection));
	void **array;
	int i;

	if ((*c)->tree_size == 0) {
		return;
	}
	/* create array of pre-order elements */
	array = (void**) malloc((*c)->data_size * (*c)->tree_size);
	_to_array((*c)->root, &array, 0, (*c)->data_size);

	initialize(&new_collection, (*c)->data_size);

	/* add each element to the new tree in pre order*/
	for (i=0; i<(*c)->tree_size; i++) {
		printf("%d: %d\n", i, *(int*)array[i]);
	}
	_add_from_array(&new_collection, array, 0, (*c)->tree_size-1, compare);
	
	/* free the old tree */
	free_collection(c);
 	/* free the array of element */
	free(array);
	/* assign the new tree to c */
	(*c)->root = new_collection->root;
	(*c)->tree_size = new_collection->tree_size;
}

void _add_from_array(Collection **c, void **array, int min_index, int max_index, int (*compare)(void *item1, void *item2)) {
	int my_index = (min_index + max_index) / 2;
	if (min_index >= max_index) {
		add(c, (array)[min_index], compare);
		return;
	}
	printf("adding: %d\t", *(int*)array[my_index]);
	add(c, (array)[my_index], compare);
	printf("calling: %d %d\n", min_index, my_index);
	_add_from_array(c, array, min_index, my_index, compare);
	printf("calling: %d %d\n", my_index, max_index);
	_add_from_array(c, array, my_index + 1, max_index, compare);
	return;
}

int _to_array(TreeNode *t, void ***array, int index, size_t size_of_element) {
	int i;
	if (t == NULL) {
		return index;
	}
	else {
		i = _to_array(t->left, array, index, size_of_element);
		(*array)[i] = malloc(size_of_element);
		(*array)[i] = t->data;
		++i;
		return _to_array(t->right, array, i, size_of_element);
	}
}

void *remove_data(Collection **c, void *data, int (*compare)(void *item1, void *item2)) {
	void *ret = malloc((*c)->data_size);
	TreeNode *my_node = (*c)->root;
	TreeNode *head = (*c)->root;
	TreeNode *parent, *parent_pred, *pred;
	int is_root = 0;

	if (!contains(*c, data, compare)) {
		return NULL;
	}
	parent = (TreeNode*) malloc(sizeof(TreeNode));
	parent->left = head;
	parent->data = malloc((*c)->data_size);
	parent->left = my_node->left;
	parent->right = my_node->right;
	memcpy(parent->data, my_node->data, (*c)->data_size);
	while (my_node) {
		if (compare(data, my_node->data) == 0) {
			parent_pred = my_node;
			pred = my_node->left;
			memcpy(ret, my_node->data, (*c)->data_size);
			if (pred != NULL) {
				while(pred->right) {
					parent_pred = pred;
					pred = pred->right;
				}
				memcpy(my_node->data, pred->data, (*c)->data_size);
				if (my_node == parent_pred) {
					my_node->left = pred->left;
				}
				else if (pred->left != NULL) {
					if (compare(parent_pred->data, pred->left->data) < 0) {
						parent_pred->right = pred->left;
					}
					else {
						parent_pred->left = pred->left;
					}
				}	
				else {
					parent_pred->right = pred->left;
				}
				free(pred);
			}
			else {
				if (is_root == 0) {
					(*c)->root = my_node->right;
				}
				else {
					if (parent->left == my_node) {
						parent->left = my_node->right;
					}
					else {
						parent->right = my_node->right;
					}
				}
				free(my_node);
				my_node = NULL;
			}
			(*c)->tree_size--;
			return ret;
		}
		else if (compare(data, my_node->data) < 0) {
			parent = my_node;
			my_node = my_node->left;
			is_root++;
			parent->size--;
		}
		else {
			parent = my_node;
			my_node = my_node->right;
			is_root++;
			parent->size--;
		}
	}
	return NULL;
}

void create_dot_file(const Collection *c, char *filename, void (*my_print)(void *data, char **ret)) {
	FILE *f = fopen(filename, "w");
	if (f == NULL)
	{
    	printf("Error opening file!\n");
	    exit(1);
	}

	fprintf(f, "digraph {\n");
	fprintf(f, "\tnode[shape=record]\n");
	_print_children_to_file(c->root, f, my_print);
	fprintf(f, "}\n");
	fclose(f);
}

void _print_children_to_file(const TreeNode *t, FILE *f, void (*my_print)(void *data, char **ret)) {
	char *my_data, *child_data;

	if (t == NULL) {
		return;
	}

	my_print(t->data, &my_data);
	if (t->left) {
		my_print(t->left->data, &child_data);
		fprintf(f, "\t%s:f0 -> %s:f1\n", my_data, child_data);
	}
	if (t->right) {
		my_print(t->right->data, &child_data);
		fprintf(f, "\t%s:f2 -> %s:f1\n", my_data, child_data);
	}

	_print_children_to_file(t->left, f, my_print);
	_print_children_to_file(t->right, f, my_print);
	fprintf(f, "\t%s [label=\"<f0>|<f1>%s(%zu)|<f2>\"];\n", my_data, my_data, t->size);
	return;
}

void free_collection(Collection **c) {
	_free_node(&((*c)->root));
	(*c)->root = NULL;
	(*c)->tree_size = 0;
}

void _free_node(TreeNode **t) {
	if ((*t) == NULL) {
		return;
	}
	_free_node(&((*t)->left));
	_free_node(&((*t)->right));
	free((*t)->data);
	free((*t));
	(*t) = NULL;
	return;
}

void *get_kth_smallest(const Collection *c, int k) {
	if (k > c->tree_size)
		return NULL;
	TreeNode *t = _get_kth_smallest(c->root, k);
	return t->data;
}

TreeNode *_get_kth_smallest(const TreeNode *t, int k) {
	int num_element = 1;
	if (t == NULL) {
		return (TreeNode*) t;
	}
	if (t->left != NULL)
		num_element += t->left->size;

	printf("num_element: %d\n", num_element);
	if (num_element == k) {
		return (TreeNode*) t;
	}
	else if (k < num_element) {
		return _get_kth_smallest(t->left, k);
	}

	else {
		return _get_kth_smallest(t->right, k - num_element);
	}
}