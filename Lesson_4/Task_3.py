# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# Записать в файл многочлен степени k.

from random import randint

k = int(input('Introduce your max coef:'))
resultString = ''
if k >= 0:
    while k > 0:
        if k == 1:
            resultString += f'{randint(0, 100)}*x + '
        else:
            resultString += f'{randint(0, 100)}*x^{k} + '
        k -= 1

else:
    while k < 0:
        resultString += f'{randint(0, 100)}*x^{k} + '
        k += 1
resultString += f'{randint(0, 100)} = 0'
with open("hw4.txt", '+a') as f:
    f.write(resultString + '\n')
print(resultString)
print('Your list was wrote in file.txt')
