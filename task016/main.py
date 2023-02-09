# Напишите программу, которая
# 1. удалит все символы в строке, индексы которы кратны 3

s = input('Введите слово: ')

result = ''
j = 0
for i in range(0, len(s), 3):
    result += s[j:i]
    j = i + 1
result += s[j:len(s)]

print(result)
