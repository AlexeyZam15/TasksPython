# Создайте программу для игры в "Крестики-нолики".
# 1. с ботом противником
# 2. для любого размерности поля

from random import randint


def print_field(field: list):
    for i in range(len(field)):
        print('|', end='')
        for j in field[i]:
            print(f'{j}|', end='')
        print()
        print('—' * 9)


def win_conditions(field: list, symbol: str):
    if (len(field) + len(field[0])) % 2 == 0:
        win = True
        for i in range(len(field)):
            win = win and field[i][i] == symbol
        if win:
            return True
        win = True
        for i in range(len(field)):
            win = win and field[i][len(field[i]) - i - 1] == symbol
        if win:
            return True
    for i in range(len(field)):
        win = True
        for j in range(len(field[i])):
            win = win and field[i][j] == symbol
        if win:
            return True
    for j in range(len(field[0])):
        win = True
        for i in range(len(field)):
            win = win and field[i][j] == symbol
        if win:
            return True


def counterattack_player_turns(field: list, symbol):
    max_count = len(field) - 1
    max_count_column = len(field[0]) - 1
    if (len(field) + len(field[0])) % 2 == 0:
        empty = False
        count = 0
        for i in range(len(field)):
            if field[i][i] == symbol:
                count += 1
            elif field[i][i] == ' ':
                empty_x, empty_y = i, i
                empty = True
            if count >= max_count and empty:
                return empty_x, empty_y
        empty = False
        count = 0
        for i in range(len(field)):
            if field[i][len(field[i]) - i - 1] == symbol:
                count += 1
            elif field[i][len(field[i]) - i - 1] == ' ':
                empty_x, empty_y = i, len(field[i]) - i - 1
                empty = True
            if count >= max_count and empty:
                return empty_x, empty_y
    for i in range(len(field)):
        empty = False
        count = 0
        for j in range(len(field[i])):
            if field[i][j] == symbol:
                count += 1
            elif field[i][j] == ' ':
                empty_x, empty_y = i, j
                empty = True
        if count >= max_count_column and empty:
            return empty_x, empty_y
    for j in range(len(field[0])):
        empty = False
        count = 0
        for i in range(len(field)):
            if field[i][j] == symbol:
                count += 1
            elif field[i][j] == ' ':
                empty_x, empty_y = i, j
                empty = True
        if count >= max_count and empty:
            return empty_x, empty_y


def random_bot_turn(field: list, symbol):
    max_row = len(field) - 1
    max_column = len(field[0]) - 1
    x1, y1 = randint(0, max_row), randint(0, max_column)
    while field[x1][y1] != ' ':
        x1, y1 = randint(0, max_row), randint(0, max_column)
    return x1, y1


def start():
    print('Начинается игра в крестики-нолики')
    print("Введите размер поля строки столбцы через пробел")
    rows, columns = [int(x) for x in input().split()[:2]]
    print('Кто ходит первым? 1 - игрок, 2 - бот')
    first_turn = input()
    while first_turn != '1' and first_turn != '2':
        print('Неправильный ввод')
        print('Кто ходит первым? 1 - игрок, 2 - бот')
        first_turn = input()

    print('Ходите играть с глупым или умным ботом? 1 - глупый, 2 - умный')
    bot_difficulty = input()
    while bot_difficulty != '1' and bot_difficulty != '2':
        print('Неправильный ввод')
        print('Ходите играть с глупым или умным ботом? 1 - глупый, 2 - умный')
        bot_difficulty = input()

    smart_bot = False

    if bot_difficulty == '2':
        smart_bot = True

    if first_turn == '1':
        players = ('игрок', 'бот')
        players_symbols = ('X', '0')
    else:
        players = ('бот', 'игрок')
        players_symbols = ('0', 'X')

    player_turn = True

    if first_turn == '2':
        player_turn = False
    end_game = False

    field1 = [[' '] * columns for i in range(rows)]

    turns = 0

    while not end_game and turns < rows * columns:
        print_field(field1)
        if player_turn:
            print('Ход игрока')
            x, y = [int(x) for x in input('Введите номер строки и столбца свободной ячейки: ').split()[:2]]
            while field1[x - 1][y - 1] != ' ':
                print('Неверный ввод')
                print_field(field1)
                x, y = [int(x) for x in input('Введите номер строки и столбца свободной ячейки: ').split()[:2]]
            field1[x - 1][y - 1] = players_symbols[0]
            player_turn = False
            if win_conditions(field1, players_symbols[0]):
                end_game = True
        else:
            print('Ход бота')
            if not smart_bot:
                x, y = random_bot_turn(field1, players_symbols[1])
            else:
                if (turns == 0 or turns == 1) and counterattack_player_turns(field1, players_symbols[0]) is None:
                    x = len(field1) // 2
                    y = len(field1[x]) // 2
                    if field1[x][y] != ' ':
                        x, y = random_bot_turn(field1, players_symbols[1])
                else:
                    if counterattack_player_turns(field1, players_symbols[0]) is not None:
                        x, y = counterattack_player_turns(field1, players_symbols[0]) \
                            if counterattack_player_turns(field1, players_symbols[1]) is None \
                            else counterattack_player_turns(field1, players_symbols[1])
                    else:
                        x, y = random_bot_turn(field1, players_symbols[1])
                    if x > len(field1) - 1:
                        x = 0
                    if y > len(field1[x]) - 1:
                        y = 0
            field1[x][y] = players_symbols[1]

            player_turn = True
            if win_conditions(field1, players_symbols[1]):
                end_game = True
        turns += 1

    print_field(field1)
    print('Игра закончена')
    if end_game:
        print('Победил', players[1] if turns % 2 == 0 else players[0])
    else:
        print('Ничья')
