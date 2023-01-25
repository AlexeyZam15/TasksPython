# Напишите программу, которая
# 1. на вход принимает одно число (N),
# 2. а на выходе показывает все целые числа в промежутке от -N до N.

n = int(input("Введите число: "))


def PrintAllNumbersFromMinusNToN(n: int):
    i = -n
    if n > 0:
        while i <= n:
            print(i, end=" ")
            i += 1
    elif n < 0:
        while i >= n:
            print(i, end=" ")
            i -= 1
    else:
        print(n)

PrintAllNumbersFromMinusNToN(n)
