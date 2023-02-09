# Напишитe программу которая
# 1. создаст 2 файла с сгенерированными многочленами
# 2. вычислит сумму многочленов и запишет в новый файл

from create_random_polynom import create_random_polynom

max_degree = int(input('Введите максимальную степень x: '))

with open('file1.txt', 'w') as data:
    data.write(create_random_polynom(max_degree))
    
with open('file2.txt', 'w') as data:
    data.write(create_random_polynom(max_degree))
    
with open('file1.txt', 'r') as data:
    for line in data:
        file1 = line
print(f'Первый многочлен:',file1)

with open('file2.txt', 'r') as data:
    for line in data:
        file2 = line
print('Второй многочлен:',file2)

def sum_polynoms(polynom1: str, polynom2: str):
    coeffs1 = polynom1.split(' = ')
    # print(coeffs1)
    coeffs1, eq = (coeffs1[0]).split(' + '), coeffs1[1]
    # print(coeffs1)
    
    dict1 = dict()
    for i in range(len(coeffs1)):
        try:
            dict1[coeffs1[i].split('*')[1]] = coeffs1[i].split('*')[0]
        except IndexError: dict1['c'] = coeffs1[i].split('*')[0]
    # print(dict1)
    
    for i in range(len(coeffs1)):
        coeffs1[i] = coeffs1[i].split('*x')[0]
    # print(coeffs1)
    
    coeffs2 = polynom2.split(' = ')
    # print(coeffs2)
    coeffs2 = (coeffs2[0]).split(' + ')
    # print(coeffs2)
    
    dict2 = dict()
    for i in range(len(coeffs2)):
        try:
            dict2[coeffs2[i].split('*')[1]] = coeffs2[i].split('*')[0]
        except IndexError: dict2['c'] = coeffs2[i].split('*')[0]
    # print(dict2)
    
    dictories_intersect = set((dict1.keys())).intersection(set(dict2.keys()))
    # print(dictories_set)
    
    dictories_diff = set((dict1.keys())).difference(set(dict2.keys()))
    res_dict = dict()
    
    max_dict = dict1
    # print(max_dict)
    min_dict = dict2
    # print(min_dict)
    if len(dict2) > len(dict1):
        max_dict = dict2
        min_dict = dict1
    
    dictories_intersect = reversed(sorted(set((max_dict.keys())).union(set(min_dict.keys()))))
        
    for i in dictories_intersect:
        if i in min_dict and i in max_dict:
            res_dict[i] = int(dict1[i]) + int(dict2[i])
        else: 
            if i in max_dict:
                res_dict[i] = max_dict[i]
            else: res_dict[i] = min_dict[i]
    # print(res_dict)
    
    expression_string = ''
    for i in res_dict:
        expression_string += f'{res_dict[i]}*{i} + '
    expression_string = (expression_string[:-3] + f' = 0').replace('*c','')
    # print(expression_string)
    return expression_string

with open('sum_file.txt', 'w') as data:
    data.write(sum_polynoms(file1,file2))

with open('sum_file.txt', 'r') as data:
    for line in data:
        print('Сумма многочленов:',line)