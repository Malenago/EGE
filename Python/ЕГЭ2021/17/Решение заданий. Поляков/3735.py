print('>>>>>>>>')
#К.Ю.Поляков 3735
'''
Рассматривается множество целых чисел, принадлежащих числовому отрезку
[10; 9999] , которые удовлетворяют следующим условиям:
а) Число в двоичной записи оканчивается цифрой «1»;
б) Число в двоичной записи имеет ровно 5 нулей;
в) Число делится на 3 и на 11.
Найдите количество таких чисел и максимальное из них.
В ответе запишите сначала количество, а потом максимальное число. 
'''
k = 0
mak = float('-inf')
def f(x):
    new_x = bin(x)[2:]
    if new_x.count('0') == 5:
        return 1
    else:
        return 0
for i in range(10, 9999+1):
    if f(i) and i % 3 == 0 and i % 11 == 0 and i % 2 == 1:
        k+=1
        mak = max(mak, i)
print(k, mak)
# Последняя цифра числа – это остаток от деления этого числа на основание системы счисления.
'''
Например, 212_{3} = 2+1*3+2*3^{2} = 23_{10}. Разделим 23 на основание системы 3,
получим 7 и 2 в остатке (2 – это последняя цифра числа в троичной системе).
Разделим 23 на 9 (основание в квадрате), получим 18 и 5 в остатке (5 = 12_{3}).
https://ege-study.ru/ru/ege/materialy/informatika/zadacha-16-razbor-razlichnyx-tipov-zadach/
'''
