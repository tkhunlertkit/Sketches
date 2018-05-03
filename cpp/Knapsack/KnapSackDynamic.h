#ifndef KNAPSACK_DYNAMIC
#define KNAPSACK_DYNAMIC

#include <cstring>
#include "KnapSack.h"
#include "Item.h"

class KnapSackDynamic : public KnapSack {
	private:
		typedef KnapSack super;

	public:
		KnapSackDynamic(std::string name, int capacity) : KnapSack(name, capacity) {}
		std::vector<Item*> optimize();
};

#endif