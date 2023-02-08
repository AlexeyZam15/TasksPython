# Напишите программу, которая
# 1. принимает на ввод натуральную степень k
# 2. формирует случайным образом список коэффициентов (значения от 0 до 10) многочлена 
# 3. выводит в терминал и записывает в файл многочлен степени k.

from random import randint

min = 0
max = 10

k = int(input('Введите натуральную степень k: '))
while k < 1:
    print('Введеные неверные данные')
    k = int(input('Введите натуральную степень k: '))

degrees = []
for i in range(1, k+1):
    degrees.append(i)

coeffs = []
for i in range(k):
    coeffs.append(randint(min, max))

# expression = 0
expression_string = ''
c = randint(min, max)

for i in range(k):
    if coeffs[i] > 0:
        expression_string += f'{coeffs[i]}*x^{degrees[i]} + '
    # expression += coeffs[i]*x**degrees[i]

if expression_string != '':
    if c != 0:
        expression_string += f'{c}'
    else:
        expression_string = expression_string[:-3]
    expression_string += ' = 0'
    print(expression_string)
else:
    print('Все коэффиценты многочлена равны 0')
# expression += c

with open('file.txt', 'w') as data:
     data.write(expression_string)