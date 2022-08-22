# Find the difference between the maximum and minimum values of the fractional part of the elements.
# Example: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 5, 10.01, 5.55]  # список значений
list_of_floats = [float(item % 1) for item in my_list]  # вычисление дробной части для каждого элемента
print('{:.2}'.format(min(list_of_floats)))  # Вывдод минимального числа дробной части
print('{:.2}'.format(max(list_of_floats)))  # Вывдод максимального числа дробной части
