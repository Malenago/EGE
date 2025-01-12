# К.Ю.Поляков 3148
# Условие: https://prnt.sc/1dklbkw
f = open('27-42b.txt')
n = int(f.readline())  # чтение файла


a = [[], [], []]  # объявление массива с 3 подмассивами

min_ost = [float('inf')]*10
''' Создаем массив с мин. разностями, изначально запихнув макс значения '''


for _ in range(n):
    cmb = sorted(list(map(int, f.readline().split())))  # сортированные тройки

    if abs(cmb[2]-cmb[1]) % 2 != 0:  # нечетную разницу чтобы поменять четность суммы
        min_ost.append(abs(cmb[2]-cmb[1]))  # добавляем в массив
        min_ost.sort()  # сортируем по возрастанию
        min_ost.pop()  # удаляем и возвращаем последний элемент
        
    elif abs(cmb[2]-cmb[0]) % 2 != 0:  # проделываем точно такое же для др.числа из тройки
        min_ost.append(abs(cmb[2]-cmb[0]))
        min_ost.sort()
        min_ost.pop()

    for i in range(3):  # засовываем в массив значения из сорт. троек
        a[i].append(cmb[i])  # a[i] - обращение к подмассиву


print(min_ost)  # вывод всех мин остатков
# смотрим на четность первых групп
print(sum(a[0]) % 2, sum(a[1]) % 2, sum(a[2]))

# две нечетные группы => вычитаем два первых элемента
print(sum(a[2])-min_ost[0]-min_ost[1])
