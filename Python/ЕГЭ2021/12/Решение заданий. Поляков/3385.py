print('>>>>>>>>>')
#3385 К.Ю.Поляков
'''
Исполнитель Редактор получает на вход строку цифр и преобразовывает её. Редактор может выполнять две команды, 
в обеих командах v и w обозначают цепочки символов.

1. заменить (v, w) 
2. нашлось (v)

Первая команда заменяет в строке первое слева вхождение цепочки v на цепочку w. Если цепочки v в строке нет, 
эта команда не изменяет строку. Вторая команда проверяет, встречается ли цепочка v в строке исполнителя Редактор.
Дана программа для исполнителя Редактор:

НАЧАЛО
ПОКА нашлось (8887) ИЛИ нашлось (77)
  ЕСЛИ нашлось (8887)
    ТО заменить (8887, 8)
    ИНАЧЕ заменить (77,8)
  КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ

Какая строка получится в результате применения приведённой ниже программы к строке, состоящей из 120 идущих подряд цифр 7? 
'''
stroka = '7' * 120
#print(stroka)
# ПОКА =>  while
while '8887' in stroka or '77' in stroka:
    if '8887' in stroka:
        stroka = stroka.replace('8887', '8', 1) # 1 -аргумент, в данном случае замена будет один раз при нахождении
    else:
        stroka = stroka.replace('77', '8', 1)
print(stroka)
