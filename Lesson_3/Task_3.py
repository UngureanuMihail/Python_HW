# Find the difference between the maximum and minimum values of the fractional part of the elements.
# Example: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 5, 10.01, 5.55]  # список значений
list_of_floats = [float(item % 1) for item in my_list]  # вычисление дробной части для каждого элемента
print('Ваше минимальное число - {:.2}'.format(min(list_of_floats)))  # Вывдод минимального числа дробной части
print('Ваше максимальное число - {:.2}'.format(max(list_of_floats)))  # Вывдод максимального числа дробной части
difference = max(list_of_floats) - min(list_of_floats)
print('Разнциа между числами - {:.2}'.format(difference)) # Вывдод максимального числа дробной части


def difference_fractional(num_list):  # фунция для определения разницы между дробными частами
    res_list = []  # пустой список для заполнения дробными частями
    for i in num_list:
        res_list.append(round(i % 1, 10))  # добавляем в список округленные дробные части
    num_dif = max(res_list) - min(res_list)  # разница между дробными частями
    return num_dif


list_1 = [1.1, 1.2, 3.1, 5.3, 10.04, 5.55]  # список
print(f'Разница между максимальным и минимальным значением дробной части эл-тов списка: \n'
      f'{list_1} => {difference_fractional(list_1)}')
