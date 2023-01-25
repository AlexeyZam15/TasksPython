# Напишите программу, которая
# 1. на вход принимает числа N и M
# 2. и выдаёт, является ли число N кратным числу M

n = int(input("Введите число N: "))
m = int(input("Введите число M: "))


def BoolNumbMultipleOfAnotherNumb(number: int, divider: int):
    return number % divider == 0


print(f"Число {n} кратно {m}"
      if BoolNumbMultipleOfAnotherNumb(n, m) else f"Число {n} не кратно {m}")
