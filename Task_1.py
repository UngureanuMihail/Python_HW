# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Ввод вещественного числа. Удаление точки.
real_number = input('Введите ваше число : ').replace('.', '')

# Перебираем элементы итерируемого массива и возвращаем новый массив типа int
lst_num = map(int, list(real_number))

# Вывод на экран сумму цифр в вещественном числе.
print(f'Сумма цифр вашего вещественного числа : {sum(lst_num)}')