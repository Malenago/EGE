#(№ 3734) (П. Волгин) Рассматривается множество целых чисел, принадлежащих числовому отрезку [10; 9999] , которые удовлетворяют следующим условиям:
#а) Число в двоичной записи оканчивается цифрой «1»;
#б) Число в двоичной записи имеет ровно 5 нулей;
#в) Число делится на 3 и на 11.
#Найдите количество таких чисел и максимальное из них. В ответе запишите сначала количество, а потом максимальное число.
# 3 РЕШЕНИЕ ЭТОЙ ЗАДАЧИ, САМОЕ КОРОТКОЕ
a=[x for x in range(10,10000) if (x%2==1) and ((str(bin(x)[2:]).count('0'))==5) and (x%3==0) and (x%11==0)]
print(len(a),max(a))