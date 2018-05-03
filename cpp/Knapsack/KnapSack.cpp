#include <iostream>
#include <vector>
#include <cmath>
#include "KnapSack.h"

using namespace std;

std::vector<Item*> KnapSack::optimize() {
    vector<Item*> i;
    if (computeWeight() <= capacity) {
        return i;
    }
    int n = (int) items.size();
    int maxVal = 0;
//    cout << "size of bag: " << n << endl;
    for (double j=0; j<pow(2.0,n); j++) {
        int mask = (int)j;
        int weight = 0;
        int value = 0;
        vector<Item*> temp;

        getWeightValue(mask, &weight, &value, temp);
//        printf("%d:\t\tweight: %d\tcapacity: %d\tvalue: %d\tmaxVal: %d\n", (int)j, weight, capacity, value, maxVal);
        if (weight <= capacity && value > maxVal) {
            maxVal = value;
            i = temp;
        }
    }
    removeFromBag(i);
    return i;
}

void KnapSack::removeFromBag(std::vector<Item*> i) {
    for (std::vector<Item*>::iterator it = i.begin() ; it != i.end(); ++it) {
        for (std::vector<Item*>::iterator it2 = items.begin() ; it2 != items.end(); ++it2) {
            if ((*it) == (*it2)) {
                items.erase(it2);
                break;
            }
        }

    }
}

void KnapSack::getWeightValue(int mask, int *weight, int *value, std::vector<Item*> &i) {
    *weight = 0;
    *value = 0;
    for (std::vector<Item*>::iterator it = items.begin() ; it != items.end(); ++it) {
        if (mask % 2 == 1) {
            *weight += (*it)->getWeight();
            *value += (*it)->getValue();
        }
        else {
            i.push_back(*it);
        }
        mask >>= 1;
    }
}

KnapSack::KnapSack(string name, int capacity) {
    this->name = name;
    this->capacity = capacity;
}

std::vector<Item*> KnapSack::add(Item * i) {
    addNoOpt(i);
    return optimize();
}

std::vector<Item*> KnapSack::getItems() {
    return items;
}
std::string KnapSack::getName() {
    return name;
}

void KnapSack::setItems(std::vector<Item*> i) {
    items = i;
}


int KnapSack::getCapacity() {
    return capacity;
}

void KnapSack::addNoOpt(Item * i){
    vector<Item*> removedItem;
    items.push_back(i);
    // cout << "[!!] adding " << i->toString() << endl;
}

int KnapSack::computeValue() {
    int sum = 0;
    for (std::vector<Item*>::iterator it = items.begin() ; it != items.end(); ++it) {
        sum += (*it)->getValue();
    }
    return sum;
}

int KnapSack::computeWeight() {
    int sum = 0;
    for (std::vector<Item*>::iterator it = items.begin() ; it != items.end(); ++it) {
        sum += (*it)->getWeight();
    }
    return sum;
}

int KnapSack::removeAll() {
    int sum = 0;
    cout << "removing..." << endl;
    while(!items.empty()) {
        Item * i = items.back();
        items.pop_back();
        cout << "[!!!] item deleted: " << i->toString() << endl;
        sum += i->getValue();
        delete i;
    }
    return sum;
}

void KnapSack::display() {
    cout << "displaying..." << endl;
    while(!items.empty()) {
        Item * i = items.back();
        items.pop_back();
        cout << "[!!!!] " << i->toString() << endl;
    }
}