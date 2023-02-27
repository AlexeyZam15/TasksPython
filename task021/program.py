# Телефонный справочник

from functions import *


def start():
    path = 'phone_book.txt'

    try:
        file = open(path, 'r')
    except IOError:
        file = open(path, 'w')
    finally:
        file.close()

    actions = {'1': 'чтение',
               '2': 'запись',
               '3': 'поиск',
               '4': 'изменение',
               '5': 'удаление',
               'q': 'выход'}

    functions = {'1': print_records,
                 '2': input_records,
                 '3': find_records_default,
                 '4': change_records,
                 '5': delete_records}

    action = None
    while action != 'q':
        create_csv(path)
        create_html(path)
        print('Какое действие хотите совершить?', *[f'{i} - {actions[i]}' for i in actions])
        action = input()
        while action not in actions:
            print('Какое действие хотите совершить?', *[f'{i} - {actions[i]}' for i in actions])
            action = input()
            if action not in actions:
                print('Введены неверные данные')
        if action != 'q':
            functions[action](path)
