# Напишите программу, которая
# 1. выводит случайное число из отрезка [min, max]
# 2. показывает наибольшую цифру числа.

import random

min1 = int(input("Введите число min: "))
max1 = int(input("Введите число max: "))


def LargestListIntElement(numbers=[]):
    max = 0
    i = 0
    while i < len(numbers):
        if numbers[i] > max:
            max = numbers[i]
        i += 1
    return max


def LargestDigitOfNumber(number: int):
    digits = []
    number = abs(number)
    while number > 0:
        digits.append(number % 10)
        number //= 10
    return LargestListIntElement(digits)


number1 = random.randint(min1, max1)
print(f"Случайное число = {number1}")

largestDigitOfNumber = LargestDigitOfNumber(number1)
print(f"Наибольшая цифра числа: {largestDigitOfNumber}")
