#include <stdio.h>

typedef struct TreeNode {
	struct TreeNode* left;
	struct TreeNode* right;
	void *data;
	size_t size;
} TreeNode;

typedef struct Collection {
	struct TreeNode* root;
	size_t data_size;
	size_t tree_size;
} Collection;

void initialize(Collection** c, size_t data_size);

int add(Collection** c, void *data, int (*compare)(void *item1, void *item2));

char *to_string(const Collection* c, void (*my_print)(void *data, char **ret));

int contains(const Collection* c, void *data, int (*compare)(void *item1, void *item2));

void load_balancing(Collection **c, int (*compare)(void *item1, void *item2));

void *remove_data(Collection **c, void *data, int (*compare)(void *item1, void *item2));

void create_dot_file(const Collection *c, char *filename, void (*my_print)(void *data, char **ret));

void free_collection(Collection** c);

void *get_kth_smallest(const Collection *c, int k);

/*
int add_all(Collection** c1, Collection** c2);

void clear();


int contains_all(const Collection* c);

int equals(Collection** c);

int hash_code(Collec);

int isE
*/