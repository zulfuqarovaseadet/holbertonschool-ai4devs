#include <iostream>

int main() {
    int scores[3] = {10, 20, 30};
    int total = 0;

    for (int i = 0; i <= 3; i++) {
        total += scores[i];
    }

    int* ptr;
    if (total > 50) {
        *ptr = total;
    }

    std::cout << "Nəticə: " << *ptr << std::endl;

    return 0;
}
