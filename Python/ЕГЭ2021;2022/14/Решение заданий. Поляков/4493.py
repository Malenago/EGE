x = 1 * 3**37 + 2 * 3 ** 23 + 3 * 3**20 + 4*3**4 + 5 * 3 ** 3 + 4 + 5

x_9 = ''

while x > 0:
    x_9 += str(x % 9)
    x //= 9

x_9 = x_9[::-1]

print(x_9.count('0'))
