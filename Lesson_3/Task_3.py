# Find the difference between the maximum and minimum values of the fractional part of the elements.
# Example: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def difference_fractional(num_list):  # фунция для определения разницы между дробными частями
    res_list = []  # пустой список для заполнения дробными частями
    for i in num_list:
        res_list.append(round(i % 1))  # добавляем в список округленные дробные части
    num_dif = max(res_list) - min(res_list)  # разница между дробными частями
    return num_dif


list_1 = [1.1, 1.2, 3.1, 5.3, 10.04, 5.55]  # список
print(f'Разница между максимальным и минимальным значением дробной части эл-тов списка: \n'
      f'{list_1} => {difference_fractional(list_1)}')
