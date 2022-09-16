# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

generated = []
factorial = lambda x: 1 if x == 0 else x * factorial(x - 1)
for i in range(1, 5):
    generated.append(factorial(i))
print(generated)
