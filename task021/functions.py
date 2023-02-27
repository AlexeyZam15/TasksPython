def print_records(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            print(*line.split(';'), end='')


def confirmation(text: str):
    confirm = input(f"Подтвердите {text} записи: y - да, n - нет\n")
    while confirm not in ('y', 'n'):
        print('Введены неверные данные')
        confirm = input(f"Подтвердите {text} записи: y - да, n - нет\n")
    return confirm


def input_records(file_name: str):
    with open(file_name, 'r+', encoding='utf-8') as data:
        record_id = 0
        for line in data:
            if line != '':
                record_id = line.split(';', 1)[0]
        print('Введите фамилию, имя, отчество, номер телефона через пробел')
        line = f'{int(record_id) + 1};' + ';'.join(input().split()[:4])
        print(*line.split(';'))
        confirm = confirmation('добавление')
        if confirm == 'y':
            data.write(line + '\n')


def find_characteristic():
    print('Выберите характеристику:')
    print('0 - id, 1 - фамилия, 2 - имя, 3 - отчество, 4 - номер, q - выйти')
    characteristic = input()
    while characteristic not in ('0', '1', '2', '3', '4', 'q'):
        print('Введены неверные данные')
        print('Выберите характеристику:')
        print('0 - id, 1 - фамилия, 2 - имя, 3 - отчество, 4 - номер, q - выйти')
        characteristic = input()
    if characteristic != 'q':
        condition = input('Введите значение\n')
        return characteristic, condition
    else:
        return 'q', 'q'


def find_records(file_name: str, characteristic, condition):
    if condition != 'q':
        printed = False
        with open(file_name, 'r', encoding='utf-8') as data:
            for line in data:
                if condition == line.split(';')[int(characteristic)].replace('\n', ''):
                    print(*line.split(';'), end='')
                    printed = True
        if not printed:
            print("Не найдено")
        return printed


def find_records_default(file_name: str):
    find_records(file_name, *find_characteristic())


def check_id_record(file_name: str, text: str):
    decision = input(f'Вы знаете id записи которую хотите {text}? 1 - да, 2 - нет, q - выйти\n')
    while decision not in ('1', 'q'):
        if decision != '2':
            print('Введены неверные данные')
        else:
            find_records(file_name, *find_characteristic())
        decision = input(f'Вы знаете id записи которую хотите {text}? 1 - да, 2 - нет, q - выйти\n')
    if decision == '1':
        record_id = input('Введите id, q - выйти\n')
        while not find_records(file_name, '0', record_id) and record_id != 'q':
            record_id = input('Введите id, q - выйти\n')
        return record_id
    return decision


def replace_record_line(file_name: str, record_id, replaced_line: str):
    replaced = ''
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            replaced += line
            if record_id == line.split(';', 1)[0]:
                replaced = replaced.replace(line, replaced_line)
    with open(file_name, 'w', encoding='utf-8') as data:
        data.write(replaced)


def change_records(file_name: str):
    record_id = check_id_record(file_name, 'изменить')
    if record_id != 'q':
        replaced_line = f'{int(record_id)};' + ';'.join(
            input('Введите фамилию, имя, отчество, номер телефона через пробел\n').split()[:4]) + ';\n'
        confirm = confirmation('изменение')
        if confirm == 'y':
            replace_record_line(file_name, record_id, replaced_line)


def delete_records(file_name: str):
    record_id = check_id_record(file_name, 'удалить')
    if record_id != 'q':
        confirm = confirmation('удаление')
        if confirm == 'y':
            replace_record_line(file_name, record_id, '')


def create_csv(file_name: str):
    with open(file_name.replace('txt', 'csv'), 'w', encoding='utf-8') as data:
        content = '"id";"Имя";"Фамилия";"Отчество";"Номер"\n'
        with open(file_name, 'r', encoding='utf-8') as data2:
            for line in data2:
                content += line
        data.write(content)


def create_html(file_name: str):
    html = \
        '''<html>
        <head>
        <meta charset="utf-8">
        <title>Телефонная книга</title>
        <link href="styles/style.css" rel="stylesheet" type="text/css">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=PT+Serif&display=swap" rel="stylesheet">
        </head>
        <body>
        <img align="left" src="https://cdn.voxlink.ru/wp-content/uploads/2018/12/1546008317_feature_image.png">
            <table>
              <tr>
                <th align="left">id</th>
                <th align="left">Имя</th>
                <th align="left">Фамилия</th>
                <th align="left">Отчество</th>
                <th align="left">Номер</th>
              </tr>'''
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            html += '''
              <tr>'''
            for cell in line.split(';'):
                html += '''
                '''
                html += f'<td>{cell}</td>'.replace('\n', '')
            html += '''
              </tr>'''

    html += '''
            </table>
        </body>
</html>'''

    with open(file_name.replace('txt', 'html'), 'w', encoding='utf-8') as page:
        page.write(html)
