# Напишите программу, которая
# 1. принимает на ввод натуральное число N.
# 2. составит список простых множителей числа N с помощью рекурсии.
# 3. составит список простых множителей числа N последовательно.
# 4. сравнить время выполнение программ

from datetime import datetime
import time


def prime_factors_number_list(number, mult=2, prime_factors=list(), log=False):
    if number == 1:
        return []
    number1 = number
    while number1 % mult == 0 and number1 // mult > 1:
        prime_factors.append(mult)
        number1 //= mult
    if log == True:
        print(*prime_factors, number1)
    for i in range(2, number1):
        if number1 % i == 0 and number1 // i > 1:
            # print(i)
            return prime_factors_number_list(number1, i, prime_factors, log)
    prime_factors.append(number1)
    return prime_factors


n = int(input('Введите натуральное число N: '))
while n <= 0:
    print('Введены неверные данные')
    n = int(input('Введите натуральное число N: '))

start_time = datetime.now()

print(*prime_factors_number_list(n, log=False))

print(f'Рекурсия - {(datetime.now() - start_time).microseconds} микросекунд')

start_time = datetime.now()

number = n
multiplier = 2
multi_list = []
while multiplier != number:
    if number % multiplier == 0:
        multi_list.append(multiplier)
        number //= multiplier
    else:
        multiplier += 1
multi_list.append(number)
print(*multi_list)

print(
    f'Последовательно - {(datetime.now() - start_time).microseconds} микросекунд')
