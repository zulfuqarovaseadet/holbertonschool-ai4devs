#include <iostream>
#include <vector>

int main() {
    std::vector<int> v = {10, 20, 30};
    // Xəta: v.at(10) mövcud deyil, proqram "std::out_of_range" xətası verəcək.
    std::cout << v.at(10) << std::endl; 
    return 0;
}
