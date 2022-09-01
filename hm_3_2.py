# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


# list_one = [2, 3, 5, 6]
# list_two = []
#
# for el in range(len(list_one)):
list_one = [2, 3, 4, 5, 6, 1, 1]
l = 5
list_two = []

while l > 0:
    if len(list_one) > 2:
        el = list_one.pop() * list_one.pop(0)
        list_two.append(el)
        l -= 1
    else:
        el = list_one[0] * list_one[0]
        list_two.append(el)
        l -= 1
print(list_two)
