# Напишите программу, которая 
# 1. примет на ввод число size
# 2. создаст список из случайных чисел размером size
# 3. примет на ввод число divider
# 4. создаст список из остатков деления чисел первого списка на число divider, если он есть. Если остатка нет, будет содержать "Нет"

from random import randint

min = 0
max = 99

size1 = int(input('Введите размер списка: '))

numbers1 = []
for i in range(size1):
    numbers1.append(randint(min,max))
print(numbers1)

divider1 = int(input('Введите число-делитель: '))

def remainders_numbers_list(numbers: list, divider: int):
    remainders = []
    for i in range(len(numbers)):
        if numbers[i] % divider == 0:
            remainders.append('Нет')
        else:
            remainders.append(numbers[i] % divider)
    return remainders

remainders_numbers1 = remainders_numbers_list(numbers1,divider1)
print(remainders_numbers1)