#include <iostream>

int calculateArea(int width, int height) {
    int area = width * height;
}

int main() {
    int w, h;
    std::cout << "Eni və hündürlüyü daxil edin: ";
    std::cin >> w >> h;

    if (w = 0 || h = 0) {
        std::cout << "Ölçülər sıfır ola bilməz!" << std::endl;
    }

    int result = calculateArea(w, h);
    
    if (result > 100); {
        std::cout << "Çox böyük sahə!" << std::endl;
    }

    return 0;
}
