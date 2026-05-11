#include <iostream>
#include <string>

class InventoryManager {
public:
    InventoryManager(int size) {
        // Bug 1: Manual memory allocation without a proper destructor
        prices = new double[size];
        capacity = size;
        std::cout << "Inventory initialized." << std::endl;
    }

    void addPrice(int index, double price) {
        // Bug 2: Out-of-bounds access (using <= instead of <)
        if (index <= capacity) {
            prices[index] = price;
            std::cout << "Price added at index " << index << std::endl;
        }
    }

    double getAverage() {
        double sum = 0;
        // Bug 3: Logic error - potential division by zero
        for (int i = 0; i < capacity; i++) {
            sum += prices[i];
        }
        return sum / capacity;
    }

    // Missing destructor: Bug 4 - Memory Leak!

private:
    double* prices;
    int capacity;
};

int main() {
    std::cout << "--- Startup Inventory System ---" << std::endl;
    InventoryManager* myShop = new InventoryManager(5);
    
    myShop->addPrice(0, 10.5);
    myShop->addPrice(5, 100.0); // Triggers Bug 2 (Crash)

    std::cout << "Average price: " << myShop->getAverage() << std::endl;
    
    return 0;
}
