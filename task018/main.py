# Напишите программу, которая
# 1. принимает на ввод координаты двух отрезков на числовой прямой
# 2. находит координаты пересечения отрезков.

def find_segments_intersection(a1, b1, a2, b2):
    res = ''

    if b1 < a2 or b2 < a1:
        return 'нет'
    elif a1 == a2 or a2 < a1 < b2 or a1 == b2:
        res += f'{a1}'
    elif a1 < a2 < b2 or a2 == b1:
        res += f'{a2}'

    if not (b1 < a2 or b2 < a1) and a2 != b1:
        if a1 == a2 or a2 < a1 < b2 or a1 < a2 < b2:
            if a2 < b1 <= b2:
                res += f' {b1}'
            else:
                res += f' {b2}'
    return res


print("Введите координаты первого отрезка через пробел")
a_1, b_1 = [int(x) for x in input().split()[:2]]
print("Введите координаты второго отрезка через пробел")
a_2, b_2 = [int(x) for x in input().split()[:2]]

res1 = find_segments_intersection(a_1, b_1, a_2, b_2)
print("Координаты пересечения")
print(res1)
