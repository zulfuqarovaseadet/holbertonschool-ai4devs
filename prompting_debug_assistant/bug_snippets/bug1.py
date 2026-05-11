import time

class UniversityManagement:
    def __init__(self, name):
        self.uni_name = name
        self.students = ["Ali", "Leyla", "Murad", "Səbinə"]
        self.grades = {"Ali": 85, "Leyla": 92, "Murad": 78}
        self.system_logs = []

    def log_event(self, message):
        timestamp = time.strftime("%H:%M:%S")
        self.system_logs.append(f"[{timestamp}] {message}")

    def show_all_students(self):
        print(f"\n--- {self.uni_name} Tələbə Siyahısı ---")
        self.log_event("Siyahı görüntüləndi")
        # Bug 1: IndexError (range(len+1) istifadəsi siyahının hüdudlarını aşır)
        for i in range(len(self.students) + 1):
            student_name = self.students[i]
            print(f"{i+1}. {student_name}")

    def add_new_student(self, name, grade):
        if name not in self.students:
            self.students.append(name)
            self.grades[name] = grade
            print(f"{name} bazaya əlavə edildi.")
            self.log_event(f"Yeni tələbə: {name}")
        else:
            print("Bu tələbə artıq qeydiyyatdadır.")

    def update_grade(self, name, new_grade):
        print(f"\nBal yenilənməsi: {name}")
        if name in self.grades:
            # Bug 2: Type Mismatch (int + str xətası)
            # 'bonus' sətir (str) olduğu üçün riyazi toplama zamanı xəta verəcək
            bonus = "10" 
            final_grade = new_grade + bonus
            self.grades[name] = final_grade
            print(f"Uğurlu! Yeni bal: {final_grade}")
        else:
            print("Xəta: Tələbə tapılmadı.")

    def calculate_average(self, data):
        print("\nStatistika hesablanır...")
        # Bug 3: ZeroDivisionError
        # Əgər data siyahısı boşdursa, len(data) sıfır olacaq və proqram çökəcək
        total_points = sum(data)
        count = len(data)
        avg = total_points / count
        return avg

    def run_system_check(self):
        print("\nSistem yoxlanışı başlayır...")
        status = "Ready"
        # Bug 4: Logical Error (Mənimsətmə '=' vs Müqayisə '==')
        # Python-da 'if' daxilində '=' istifadə etmək SyntaxError verir
        if status = "Ready":
            print("Sistem statusu: Stabil")
            self.log_event("Yoxlanış tamamlandı")

if __name__ == "__main__":
    bdu = UniversityManagement("Bakı Dövlət Universiteti")
    
    # 1. ZeroDivisionError yoxlaması
    try:
        print("Ortalama:", bdu.calculate_average([]))
    except Exception as e:
        print(f"Sistem Xətası (Avg): {e}")

    # 2. Grade Update yoxlaması
    try:
        bdu.update_grade("Ali", 80)
    except Exception as e:
        print(f"Sistem Xətası (Grade): {e}")

    # 3. Student List yoxlaması
    try:
        bdu.show_all_students()
    except Exception as e:
        print(f"Sistem Xətası (List): {e}")
