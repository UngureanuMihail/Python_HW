# Реализовать алгоритм задания случайных чисел.
import random

n = list(range(-100, 100, 1))
random.shuffle(n)
print(f'Your random number is - ({n[0]})')

# v2 Cгенерировать целое число в заданном диапазоне
random_number = random.randint(-500, 500)
print(f'Your random number is - ({random_number})')
