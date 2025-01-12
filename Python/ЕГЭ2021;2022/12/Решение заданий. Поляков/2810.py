# (№ 2810) (А.М. Кабанов) Исполнитель Редактор получает на вход строку цифр и преобразовывает её.
# Редактор может выполнять две команды, в обеих командах v и w обозначают цепочки символов.
# 1. заменить (v, w)
# 2. нашлось (v)
# Первая команда заменяет в строке первое слева вхождение цепочки v на цепочку w.
# Если цепочки v в строке нет, эта команда не изменяет строку. Вторая команда проверяет, встречается ли цепочка v в строке исполнителя Редактор. Если она встречается, то команда возвращает логическое значение "истина", в противном случае возвращает значение "ложь".
# Дана программа для исполнителя Редактор:
# НАЧАЛО
# ПОКА нашлось (1111)
#  заменить (1111, 7)
#  заменить (77, 1)
# КОНЕЦ ПОКА
# КОНЕЦ
# Какая строка получится в результате применения приведённой программы к строке вида 1…17…7 (95 единиц и 31 семёрка)?
s = '1'*95+'7'*31

while '1111' in s:
    s = s.replace('1111', '7', 1)
    s = s.replace('77', '1', 1)

print(s)
