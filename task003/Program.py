# Напишите программу, которая 
# 1. на вход принимает число от 1 до 7
# 2. будет выдавать название дня недели по заданному номеру.

while True:
    day = int(input("Введите номер дня недели: "))
    if day > 7:
        print("Введены неверные данные")
    elif day < 0:
        print("Введены неверные данные")
    else:
        break

if day == 1:
    print("Понедельник")
elif day == 2:
    print("Вторник")
elif day == 3:
    print("Среда")
elif day == 4:
    print("Четверг")
elif day == 5:
    print("Пятница")
elif day == 6:
    print("Суббота")
elif day == 7:
    print("Воскресенье")