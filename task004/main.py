# Напишите программу, которая
# 1. принимает на вход три числа
# 2. и выдаёт максимальное из этих чисел.

input_numbers_size = 3

numbers = []

i = 0
while i < input_numbers_size:
    numbers.append(int(input(f"Введите число № {i}: ")))
    i += 1

print(numbers)


def LargestNumber(numbers=[]):
    max = numbers[0]
    i = 0
    while i < len(numbers):
        if numbers[i] > max:
            max = numbers[i]
        i += 1
    return max


max = LargestNumber(numbers)

print(f"Наибольшее число: {max}")
