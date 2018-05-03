#include <stdio.h>
#include <time.h>
#include <stdlib.h>

#define NUM_ELEMENT 10000000
#define NUM_ITERATION 1

void print_a(int *a) {
  int i;
  for (i=0; i<NUM_ELEMENT; ++i) {
      printf("%d ", a[i]);
  }
  printf("\n");
}

void quicksort(int **a, int size, int left, int right) {
  int p = (*a)[right];
  int i = left;
  int j = right;
  if (i >= j || i < 0) {
    return;
  }

  while (i < j) {
    while ((*a)[i] <= p && i < j) {
      ++i;
    }
    while ((*a)[j] >= p && i < j) {
      --j;
    }
    if (i < j) {
      int temp = (*a)[i];
      (*a)[i] = (*a)[j];
      (*a)[j] = temp;
    }
  }

  if ((*a)[i] > p) {
    (*a)[right] = (*a)[i];
    (*a)[i] = p;
  }
  quicksort(a, i - left, left, i-1);
  quicksort(a, right - i, i+1, right);
}

int main() {
  srand(time(NULL));
  int i, j;
  for (i=0; i<NUM_ITERATION; ++i) {
    int *a = (int*) malloc(sizeof(int) * NUM_ELEMENT);
    for (j=0; j<NUM_ELEMENT; ++j) {
      a[j] = rand() % (NUM_ELEMENT * 200);
    }

    quicksort(&a, NUM_ELEMENT, 0, NUM_ELEMENT - 1);

  }
  printf("DONE !!!!\n");


}
