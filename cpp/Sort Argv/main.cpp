#include <iostream>
#include <string.h>

using namespace std;

void swap(char **p, char **q) {
    char *tmp = *p;
    *p = *q;
    *q = tmp;
}

void printArray(char ** arr) {
    for (char **p = arr; *p != NULL; p++) {
        cout << *p << endl;
    }
}

int main(int argc, char ** argv) {
    char **p, **q, **minSoFar;

    for (p = argv + 1; *p != NULL; p++) {
        minSoFar = p;
        for (q = p + 1; *q != NULL; q++) {
            if (strcmp(*q, *p) < 0) {
                minSoFar = q;
            }
        }
        q = (char**) malloc(sizeof(char*));
        *q = *p;
        *p = *minSoFar;
        *minSoFar = *q;
        // swap(minSoFar, p);
    }
    printArray(argv+1);
}