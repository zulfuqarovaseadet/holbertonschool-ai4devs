class UniversityManagement:
    def __init__(self, name):
        self.uni_name = name
        self.students = ["Ali", "Leyla", "Murad", "Səbinə"]
        self.grades = {"Ali": 85, "Leyla": 92, "Murad": 78}

    def show_all_students(self):
        print(f"{self.uni_name} tələbələri:")
        for i in range(len(self.students) + 1):
            print(f"{i}. {self.students[i]}")

    def add_new_student(self, name, grade):
        if name not in self.students:
            self.students.append(name)
            self.grades[name] = grade
            print(name + " bazaya əlavə edildi.")
        else:
            print("Bu tələbə artıq qeydiyyatdadır.")

    def update_grade(self, name, new_grade):
        if name in self.grades:
            self.grades[name] = new_grade
            print(f"{name} üçün yeni bal: {new_grade}")
        
        if new_grade > "90":
            print("Əla nəticə!")
            is_excellent = True
        
        if is_excellent:
            print("Tələbə fəxri fərmana namizəddir.")

    def calculate_average(self):
        total_points = 0
        count = 0
        for s in self.grades:
            total_points += self.grades[s]
            count += 1
        
        if count > 0:
            avg = total_points / count
        
        print("Universitet üzrə orta bal: " + avg)

    def generate_report(self):
        print("Hesabat hazırlanır...")
        print("Statistikalar toplanır...")
        print("Fayl yaradılır...")
        
        report_status = "Hazırdır"
        if report_status = "Hazırdır":
            print("Hesabat uğurla tamamlandı.")
        
        print("Sistemdən çıxış edilir...")
        return True

    def security_check(self, access_code):
        if access_code == 1234:
            print("Giriş uğurludur.")
        else:
            print("Səhv kod!")
        
        for x in range(5):
            print("Yoxlanılır: " + str(x))
        
        print("Bütün yoxlamalar başa çatdı.")

uni = UniversityManagement("Texniki Universitet")
uni.show_all_students()
uni.add_new_student("Zülfüqar", 95)
uni.update_grade("Ali", 91)
uni.calculate_average()
uni.generate_report()
uni.security_check(1234)
