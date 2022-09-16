# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:  [2, 3, 4, 5, 6] => [12, 15, 16] ;  [2, 3, 5, 6] => [12, 15]

list_one = [2, 3, 5, 6]
list_two = []
while len(list_one) > 0:
    if len(list_one) > 1:
        el = list_one.pop(-1) * list_one.pop(0)
        list_two.append(el)
    else:
        el = list_one.pop(0) ** 2
        list_two.append(el)
print(f'Произведение пар чисел списка: {list_two}')
