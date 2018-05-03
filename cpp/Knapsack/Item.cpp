#include "Item.h"
#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <sstream>

Item::Item(const char *s, int weight, int value) {
    strcpy(this->name, s);
    this->weight = weight;
    this->value = value;
}

int Item::getWeight() {
    return weight;
}

int Item::getValue() {
    return value;
}

char* Item::getName() {
    return name;
}

const char* Item::toString() {
    std::string n (name);
    std::stringstream out;
    out << weight;
    std::string w = out.str();
    out.str(std::string());
    out << value;
    std::string v = out.str();
    std::string s = n + " with weight of " + w + " with value of " + v;
    return s.c_str();
}

Item::~Item() {}