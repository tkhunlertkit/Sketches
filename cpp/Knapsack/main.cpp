#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <vector>
#include "KnapSack.h"
#include "Item.h"
#include "KnapSackDynamic.h"

using namespace std;

#define NUM_ITEMS 20
#define MAX_WEIGHT 10
#define MAX_VALUE 30
#define CAPACITY 10

int randomWeight() {
    return rand() % MAX_WEIGHT + 1;
}

int randomValue() {
    return rand() % MAX_VALUE + 1;
}

void print(KnapSack *ks, vector<Item*> unUsed, int *totalWeight, int *totalValue) {
    cout << "---------- KnapSack " << ks->getName() << " ----------" << endl;
    cout << "Unused by " << ks->getName() << endl;
    for (std::vector<Item*>::iterator it = unUsed.begin() ; it != unUsed.end(); ++it) {
        // cout << (*it)->toString() << endl;
        delete (*it);
    }
    *totalWeight = ks->computeWeight();
    *totalValue = ks->computeValue();
    ks->removeAll();
    cout << "------ Done KnapSack " << ks->getName() << " ----------" << endl;
    cout << endl;
}

int main(int argc, const char* argv[]) {
    clock_t start, end;
    srand (time(NULL));
    string s;
    int ii;
    vector<Item*> useless;
    double seconds_bf, seconds_dp;

    Item *i1, *i2, *i3;
    KnapSack *ks = new KnapSack("Greedy", CAPACITY);
    KnapSack *ks2 = new KnapSack("Brute Force", CAPACITY);
    KnapSackDynamic *ks3 = new KnapSackDynamic("Dynamic", CAPACITY);

    for (ii=0; ii<NUM_ITEMS; ii++) {
        s = "";
        for (int j=0; j<5; j++) {
            int r = (int)(rand() % 26 + 65);
            s += (char)r;
        }
        int tempWeight = randomWeight();
        int tempValue = randomValue();
        i1 = new Item(s.c_str(), tempWeight, tempValue);
        i2 = new Item(s.c_str(), tempWeight, tempValue);
        i3 = new Item(s.c_str(), tempWeight, tempValue);
        vector<Item*> li = ks->add(i1);
        ks2->addNoOpt(i2);
        ks3->addNoOpt(i3);
        if (!li.empty()) {
            for (std::vector<Item*>::iterator it = li.begin() ; it != li.end(); ++it) {
                // cout << (*it)->toString() << endl;
                useless.push_back(*it);
            }
        }
    }

    int totalWeightGreedy, totalValueGreedy;
    int totalWeightBrute, totalValueBrute;
    int totalWeightDynamic, totalValueDynamic;

    print(ks, useless, &totalWeightGreedy, &totalValueGreedy);

    start = clock();
    vector<Item*> li = ks2->optimize();
    end = clock();
    seconds_bf = 1000.0 * (end - start) / CLOCKS_PER_SEC;
    print(ks2, li, &totalWeightBrute, &totalValueBrute);


    start = clock();
    vector<Item*> li2 = ks3->optimize();
    end = clock();
    seconds_dp = 1000.0 * (end - start) / CLOCKS_PER_SEC;
    print(ks3, li2, &totalWeightDynamic, &totalValueDynamic);
    
    cout << ks->getName() << ": \ttotal value is: " << totalValueGreedy << " with weight of: " << totalWeightGreedy << endl;
    cout << ks2->getName() << ": \ttotal value is: " << totalValueBrute << " with weight of: " << totalWeightBrute << endl;
    cout << ks3->getName() << ": \ttotal value is: " << totalValueDynamic << " with weight of: " << totalWeightDynamic << endl;

    cout << endl;
    cout << "brute force took " << seconds_bf << " ms" << endl;
    cout << "Dynamic Programming took " << seconds_dp << " ms" << endl;
    
    delete ks;
    delete ks2;
    delete ks3;
    return 0;
}
