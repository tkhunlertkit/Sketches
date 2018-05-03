#include <iostream>
#include "bb.h"

using namespace std;

void bbbb::print() {
	cout << "b: " << super::getB() << " then a: " << super::getA() << endl;
}