Bug 1: Python - University Management
​File: bug1.py
​Error 1: range(len(self.students) + 1) – Siyahının ölçüsündən kənara çıxma xətası (IndexError).
​Error 2: new_grade > "90" – Tam ədəd (int) ilə sətir (str) müqayisə edilərkən TypeError baş verir.
​Error 3: is_excellent dəyişəni yalnız if daxilində yaradılıb; şərt ödənmədikdə aşağıda NameError verir.
​Error 4: if report_status = "Hazırdır" – Müqayisə əvəzinə mənimsətmə operatoru istifadə edilib.
​Bug 2: Java - Student Management
​File: bug2.java
​Error 1: i <= students.size() – ArrayList ölçüsünü keçdiyi üçün IndexOutOfBoundsException yaradır.
​Error 2: String status dəyişəni if daxilində lokaldır, çöldə istifadəsi kompilyasiya xətası verir.
​Error 3: average = 90 – if şərtində mənimsətmə operatoru istifadə edilib.
​Error 4: logMessage.length() – null dəyişən üzərində metod çağırıldığı üçün NullPointerException verir.
​Bug 3: C++ - Data Processor (Memory)
​File: bug3.cpp
​Error 1: i <= dataSize – Massivin hüdudlarından kənara çıxma (Buffer Overflow).
​Error 2: int* tempPtr – Ünvan mənimsədilməmiş pointerə (wild pointer) qiymət yazmağa çalışmaq.
​Error 3: delete dataPointer – Massivlər üçün delete[] istifadə olunmalıdır.
​Error 4: Use-after-free – Yaddaşdan silinmiş dataPointer[0] elementini oxumağa çalışmaq.
​Bug 4: C++ - Grade Calculator (Logic)
​File: bug4.cpp
​Error 1: calculateFinal funksiyasında return yoxdur; bu, qeyri-müəyyən nəticə qaytarır.
​Error 2: if (score = 51) – Şərt daxilində mənimsətmə, nəticə həmişə true olur.
​Error 3: if (studentCount < 0); – Artıq qoyulan ; işarəsi if şərtini mənasız edir, blok həmişə icra olunur.
​Bug 5: Python - Bank System
​File: bug5.py
​Error 1: range(len(self.transaction_history) + 1) – Dövr massiv sərhədlərini aşır (IndexError).
​Error 2: print("Yeni balans: " + self.balance) – String və Float birləşdirilə bilməz (TypeError).
​Error 3: amount > "500" – Rəqəmlə mətni müqayisə etmək mümkün deyil.
​Error 4: if confirm = "Bəli" – Məntiqi müqayisə əvəzinə mənimsətmə xətası.
