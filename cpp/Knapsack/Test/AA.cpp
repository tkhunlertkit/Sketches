#include <iostream>
#include "AA.h"

using namespace std;


aaaa::aaaa(int a, int b) {
	this->a = a;
	this->b = b;
}

void aaaa::print() {
	cout << "a: " << this->a << " then b: " << this->b << endl;
}

int aaaa::getA() {
	return a;
}

int aaaa::getB() {
	return b;
}