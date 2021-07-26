#(№ 2674) (Д.В. Богданов) Имеется набор данных, состоящий из положительных целых чисел.
#Необходимо определить количество пар элементов (ai, aj) этого набора, в которых 1 ≤ i < j ≤ N и сумма элементов кратна 12.
f=open('файлик')
n=int(f.readline())

d=[0]*12
count_pair=0

for _ in range(n):
    x=int(f.readline())

    for i in range(12):
        if (x+i)%12==0:
            count_pair+=d[i]

    d[x%12]+=1

print(count_pair)

