# Напишите программу, которая
# 1. принимает на вход число N и число K, которое должно быть меньше кол-ва цифр в числе N
# 2. и на выходе показывает K-ую цифру этого числа.
# Выполнить с помощью числовых операций (целочисленное деление, остаток от деления).

def determine_number_digits(number):
    number = abs(number)
    count = 1
    while number > 9:
        count += 1
        number //= 10
    return count


def find_number_digit(number, digit_number):
    number = abs(number)
    count_digits = determine_number_digits(number)
    for i in range(count_digits-digit_number):
        number //= 10
    return number % 10


n = int(input("Введите число: "))

count_digits1 = determine_number_digits(n)
k = 0
while True:
    print(f"В числе цифр: {count_digits1}")
    k = int(input("Введите номер цифры: "))
    if k >= 1 and k <= count_digits1:
        break
    else:
        print('Введено неверное число')

number_digit1 = find_number_digit(n, k)
print(f'Цифра числа под номером {k}: {number_digit1}')
