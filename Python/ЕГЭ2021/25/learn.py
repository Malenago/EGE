#Всем привет, познакомимся с основами. Самое простое задание из 2 части

#Проверка на простоту числа. Проверена мною на миллионных значениях чисел
def f(x):
    sq = int(x**0.5)
    for i in range(2, sq+1):
        if x % i == 0:
            return False #число делится, дальше можно не проверять
    return True #программа до сих пор в функции? простое, давайте отправим гуд
print(f(5))
print(f(25))


def F(x):
    delet = set() # множества хранят ток уникальные значения(делители), ничего лишнего
    sq = int(x**0.5)+1 #поч мы идем до корня? сейчас посмотрите ниже как мы ищем делители
    for i in range(1, sq+1):
        if x % i == 0:
            delet.add(i)
            delet.add(x//i)
    print(delet)
    return 'Coooool'
F(25)


'''  Это основа. Остальное от задачи к задаче'''

print('Предупреждение: вы близки к сотке')
