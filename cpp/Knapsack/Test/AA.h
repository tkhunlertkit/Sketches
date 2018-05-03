#ifndef AA
#define AA

#include "InterfaceAA.h"

class aaaa : public InterfaceAA{
// class aaaa {
	private:
		int a, b;

    public:
        aaaa(int a, int b);
        void print();

    protected:
    	int getA();
    	int getB();
};

#endif