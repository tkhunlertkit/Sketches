#ifndef ITEM
#define ITEM

class Item {
    private:
        char name[50];
        int weight;
        int value;

    public:
        Item(const char* s, int weight, int value);
        int getWeight();
        int getValue();
        char* getName();
        const char* toString();
        ~Item();
};

#endif