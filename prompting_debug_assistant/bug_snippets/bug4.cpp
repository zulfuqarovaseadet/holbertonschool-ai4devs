#include <iostream>
#include <string>

class GradeCalculator {
public:
    double calculateFinal(double mid, double fin) {
        double total = (mid * 0.4) + (fin * 0.6);
        // BUG 1: Missing return statement (Funksiya dəyər qaytarmalıdır)
    }

    void checkStatus(double score) {
        // BUG 2: Assignment in condition (score = 51 həmişə true qaytarır)
        if (score = 51) {
            std::cout << "Tələbə keçdi." << std::endl;
        } else if (score < 51) {
            std::cout << "Tələbə kəsildi." << std::endl;
        }
    }

    void processReport(int studentCount) {
        std::cout << "Hesabat hazırlanır..." << std::endl;
        
        // BUG 3: Extra semicolon after IF (Şərt blokunu vaxtından əvvəl bitirir)
        if (studentCount < 0); {
            std::cout << "XƏTA: Tələbə sayı mənfi ola bilməz!" << std::endl;
        }

        std::cout << "Sistem loqları:" << std::endl;
        std::cout << "--- Log 1: Fayl açıldı." << std::endl;
        std::cout << "--- Log 2: Verilənlər oxundu." << std::endl;
        std::cout << "--- Log 3: Hesablama aparıldı." << std::endl;
        std::cout << "--- Log 4: Fayl bağlandı." << std::endl;
    }
};

int main() {
    GradeCalculator calc;
    double m = 40.0;
    double f = 60.0;

    double result = calc.calculateFinal(m, f);
    std::cout << "Yekun bal: " << result << std::endl;

    calc.checkStatus(result);
    calc.processReport(10);

    std::cout << "Əməliyyat uğurla başa çatdı." << std::endl;
    std::cout << "Çıxış üçün bir düyməyə basın..." << std::endl;
    
    for(int i=0; i<5; i++) {
        std::cout << "Sistem bağlanır: " << 5-i << std::endl;
    }

    return 0;
}
