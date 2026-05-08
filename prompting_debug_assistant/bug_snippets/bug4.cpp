#include <iostream>

int main() {
    int* ptr = nullptr;
    // Xəta: Null olan yaddaş ünvanını oxumağa çalışır (Segmentation fault).
    std::cout << *ptr << std::endl; 
    return 0;
}
