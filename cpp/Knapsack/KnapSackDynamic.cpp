#include <vector>
#include <algorithm>
#include <iostream>

#include "KnapSackDynamic.h"
#include "Item.h"

using namespace std;

std::vector<Item*> KnapSackDynamic::optimize() {
	std::vector<Item*> rm;
	std::vector<Item*> inc;
	int n = super::getItems().size();
	int capacity = super::getCapacity();

	int **v = (int**) malloc(sizeof(int*) * (n + 1));
	for (int i=0; i<=n; ++i) {
		v[i] = (int*) malloc(sizeof(int) * (capacity + 1));
	}

	int **keep = (int**) malloc(sizeof(int*) * (n + 1));
	for (int i=0; i<=n; ++i) {
		keep[i] = (int*) malloc(sizeof(int) * (capacity + 1));
	}

	for (int j=0; j<=capacity; ++j) {
		for (int w=0; w<=n; w++) {
			v[w][j] = 0;
		}
	}

	for (int i=1; i<=n; i++) {
		Item * current = super::getItems()[i-1];
		// cout << current->toString() << endl;
		int value_i = current->getValue();
		int weight_i = current->getWeight();
		for (int w=0; w<=capacity; w++) {
			if (weight_i <= w && value_i + v[i-1][w-weight_i] > v[i-1][w]) {
				v[i][w] = value_i + v[i-1][w-weight_i];
				keep[i][w] = 1;
			}
			else {
				v[i][w] = v[i-1][w];
				keep[i][w] = 0;
			}
		}
	}
	int k = capacity;
	for (int i=n; i>=1; --i) {
		if (keep[i][k] == 1) {
			Item * current = super::getItems()[i-1];
			inc.push_back(current);
			k = k - current->getWeight();
		}
	}

	super::removeFromBag(inc);
	rm = super::getItems();
	super::setItems(inc);



	return rm;

}