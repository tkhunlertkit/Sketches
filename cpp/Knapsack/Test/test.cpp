#include <iostream>
#include <vector>

#include "AA.h"
#include "BB.h"

using namespace std;

// void print(vector<int> a) {
// 	for (vector<int>::iterator it = a.begin(); it != a.end(); ++it) {
// 		cout << (*it) << " ";
// 	}
// 	cout << endl;
// }


int main(int argc, const char * argv[]) {
	// vector<int> a;
	// a.push_back(1);
	// a.push_back(2);
	// a.push_back(3);
	// print(a);
	// a[2] = 5;
	// print(a);

	aaaa *my_a = new aaaa(1,2);
	my_a->print();
	bbbb *my_b = new bbbb(4,3);
	my_b->print();

	int row = 5;
	int col = 6;

	int **array = (int**) malloc(sizeof(int*) * row);
	for (int i=0; i<row; ++i) {
		array[i] = (int*) malloc(sizeof(int) * col);
	}

	for (int i=0; i<row; ++i) {
		for (int j=0; j<col; ++j) {
			array[i][j] = i + j;
			// cout << i << " " << j << " = " << array[i][j] << endl;
		}
	}

	for (int i=0; i<row; ++i) {
		for (int j=0; j<col; ++j) {
			cout << array[i][j] << " ";
		}
		cout << endl;
	}


}