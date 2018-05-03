#ifndef KNAPSACK
#define KNAPSACK

#include <vector>
#include <cstring>
#include "Item.h"


class KnapSack {
    private:
        std::string name;
        int capacity;
        std::vector<Item*> items;
        void getWeightValue(int mask, int *weight, int *value, std::vector<Item*> &i);

    protected:
        void removeFromBag(std::vector<Item*> i);

    public:
        KnapSack(std::string name, int capacity);
        std::vector<Item*> getItems();
        int getCapacity();
        std::string getName();
        void setItems(std::vector<Item*> i);
        std::vector<Item*> optimize();
        std::vector<Item*> add(Item * i);
        void addNoOpt(Item * i);
        int computeValue();
        int computeWeight();
        int removeAll();
        void display();
};

#endif