# Напишите программу, которая
# 1. на вход принимает числа min, max и N
# 2. на выходе показывает все, делимые на N от min до max.

min = int(input("Введите число min: "))
max = int(input("Введите число max: "))
n = int(input("Введите число n: "))


def NumbersFromMinToMaxMultipleOfNumber(min: int, max: int, divider: int):
    i = min
    numbers = []
    while i <= max:
        if i % divider == 0:
            numbers.append(i)
        i += 1
    return numbers


numbers = NumbersFromMinToMaxMultipleOfNumber(min, max, n)
print(f"Числа от {min} до {max}, делимые на {n}: \n {numbers}")
