# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
def fibonacci(n):  # функция для вычисления числа фибоначчи
    if n == 0:
        return 0  # в случае 0 возвращение 0
    elif n == 1:
        return 1  # в случае 1 возвращение 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # в любом другом случае возвращаем значение по данному принципу

# 2 вариант____________________________________

def negafibonacci(k):
    if k == -1:
        return 1  # в случае -1 возвращение 1
    elif k == -2:
        return -1  # в случае -2 возвращение -1
    elif k != 0:
        return negafibonacci(k + 2) - negafibonacci(k + 1)
        # в случае числа не равного 0 возвращаем значение по # данному принципу


num = int(input('Введите ваше число: '))
num_fib = []
for i in range(- num, 0):  # в диапазоне от - (введенное число) до 0
    num_fib.append(negafibonacci(i))  # выполняем для каждого елемента фунцию negafibonacci
for i in range(num + 1):  # в диапазоне от (от нуля до введенное число +1
    num_fib.append(fibonacci(i))
print(f'Для вашего числа = {num} -> {num_fib}')  # выполняем для каждого елемента фунцию fibonacci
