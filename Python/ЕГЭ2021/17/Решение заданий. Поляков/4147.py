print('>>>>>>')
#К.Ю.Поляков 4147
'''
Рассматривается множество целых чисел, принадлежащих числовому отрезку
[25552; 58885], которые имеют не менее 15 двузначных делителей.
Запишите в ответе сначала наибольшее из таких чисел, затем – их количество. 
'''
huge = 0
number_count = 0
for x in range(25552, 58885+1):
    q = int(x**0.5)
    d = set()
    for i in range(1, q+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    jou = 0
    for i in d:
        if len(str(i)) == 2:
            jou+=1
        if jou == 15:
            number_count+=1

            if huge < x:
                huge = x # поставьте == и поймите что произошло
                break
print(huge, number_count)
        



# =  оператор присваивания
# == оператор сравнения
# новички это постоянно путают, поэтому хотел обратить внимание