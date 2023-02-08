# Напишите программу, которая
# 1. принимает на ввод число N (не меньше 3)
# 2. принимает на ввод N чисел
# 3. определяет, являются ли заданные числа (в указанном порядке) последовательными членами арифметической прогрессии.


count_numbers = int(input('Введите кол-во чисел: '))
while count_numbers < 3:
    print('Введены неверные данные.Кол-во чисел должно быть не меньше 3')
    count_numbers = int(input('Введите кол-во чисел: '))
    
a = []
for i in range(count_numbers):
    a.append(int(input(f'Введите число № {i}: ')))

size_a = len(a)
arif = True
d = a[1] - a[0]
for i in range(size_a-2):
    # print(f'{a[i+2]} == {a[i+1]} + {a[i]}')
    if a[i+2] != a[i+1] + d:
        arif = False
if arif == True:
    print('ДА')
else: print('НЕТ')