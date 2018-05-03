#ifndef BB
#define BB

#include "AA.h"

class bbbb : public aaaa{
private:
	typedef aaaa super;
public:
	bbbb(int a, int b) : aaaa(a, b) {}
	void print();
};

#endif