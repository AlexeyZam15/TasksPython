# Напишите программу, которая
# 1. выводит случайное n-значное число
# 2. и удаляет k-ую цифру этого числа.
# Выполнить с помощью числовых операций.


import random


def number_digits_random_number(number_digits):
    min = 1
    max = 9
    return_min = min
    return_max = max
    for i in range(number_digits-1):
        return_min *= 10
        return_max = return_max * 10 + max
    return return_min, return_max


def determine_number_digits(number):
    number = abs(number)
    count = 1
    while number > 9:
        count += 1
        number //= 10
    return count


def digits_number_list(number):
    digits = []
    number_digits = determine_number_digits(number)
    for i in range(number_digits):
        digits.append(number % 10)
        number //= 10
    digits.reverse()
    return digits


def delete_number_digit(number, digit_number):

    number_digits = determine_number_digits(number)
    digits = digits_number_list(number)
    return_number = 0

    for i in range(number_digits):
        if i != digit_number-1:
            mult = 1
            for j in range(len(digits)-i-1, 0, -1):
                mult *= 10
            if i < digit_number-1:
                mult //= 10
            return_number += digits[i]*mult

    return return_number


n = 0
while n < 1:
    n = int(input('Введите количество цифр: '))
    if n < 1:
        print('Введены неверные данные')

min1, max1 = number_digits_random_number(n)

numb1 = random.randint(min1, max1)
print(f"Число: {numb1}")

count_digits1 = determine_number_digits(numb1)
digits_numb1 = digits_number_list(numb1)

k = 0
while True:
    print(f"В числе цифр: {count_digits1}")
    k = int(input("Введите номер цифры: "))
    if k >= 1 and k <= count_digits1:
        break
    else:
        print('Введено неверное число')

numb1 = delete_number_digit(numb1, k)
print(f'Изменённое число: {numb1}')
