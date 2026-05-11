Bug 1: Python - Discount Calculation
​File: bug_snippets/bug1.py
​Error 1: range(len(prices) + 1) – Siyahının ölçüsündən kənara çıxdığı üçün IndexError verir.
​Error 2: rate = "0.1" – Endirim dərəcəsi sətir (string) kimi təyin edildiyi üçün riyazi əməliyyatda TypeError yaradır.
​Error 3: final_price dəyişəni yalnız if blokunun daxilindədir; şərt ödənmədiyi halda UnboundLocalError baş verir.
​Bug 2: JavaScript - Inventory Management
​File: bug_snippets/bug2.js
​Error 1: i <= prices.length – Dövr massivin son indeksindən kənara çıxır (Undefined access).
​Error 2: average = 20 – Şərt daxilində müqayisə operatoru əvəzinə mənimsətmə istifadə edilib.
​Error 3: message.toUpperCase() – message dəyişəni null olduğu üçün TypeError yaradır.
​Bug 3: C++ - Array & Memory Access
​File: bug_snippets/bug3.cpp
​Error 1: scores[3] – 3 elementli massivdə (0,1,2) 3-cü indeksə müraciət yaddaş xətasına səbəb olur.
​Error 2: int* ptr; – Göstəriciyə (pointer) ünvan mənimsədilmədən istifadə olunub (Wild Pointer).
​Error 3: *ptr = total – Təyin olunmamış yaddaş sahəsinə yazı yazmaq proqramın çökdməsinə (Segmentation fault) səbəb olur.
​Bug 4: C++ - Logical Flow & Syntax
​File: bug_snippets/bug4.cpp
​Error 1: calculateArea funksiyasında return ifadəsi yoxdur, funksiya qeyri-müəyyən dəyər qaytarır.
​Error 2: if (w = 0) – Müqayisə (==) əvəzinə mənimsətmə (=) yazılıb, şərt həmişə sıfır (false) olur.
​Error 3: if (result > 100); – Şərtdən dərhal sonra qoyulan nöqtəli vergül məntiqi blokun işini pozur.
​Bug 5: Python - Library/User Logic
​File: bug_snippets/bug5.py
​Error 1: users.username – Lüğət elementlərinə obyekt xüsusiyyəti kimi müraciət edilə bilməz (AttributeError).
​Error 2: age > "18" – Tam ədəd (int) ilə sətir (str) müqayisə edilərkən TypeError baş verir.
​Error 3: is_valid dəyişəni yalnız müəyyən bir şərt daxilində yaradıldığı üçün proqramın digər hissələrində tapılmaya bilər.
