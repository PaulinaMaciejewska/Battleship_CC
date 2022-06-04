import os
from messages import game_messages
from parematers import ship_direction, board_maximal_rang, game_who_play, game_difficult, game_colours, board_signes, game_command
from screen_deposit import game_help, game_titele
from game_stat import game_statis_read

""" moduł sprawdzający poprawniść wpisania danych przez gracza"""

def input_validation_game_option(entry):
    """ funkcja odpowiedzialna za komendy"""
    if entry == game_command[1]:
        os.system("cls")
        print(game_titele)
        game_statis_read()
        print(game_messages["S12"])
        exit()
    elif entry == game_command[2]:
        print(game_help)
        input(game_messages["I15"])
        return entry
    elif entry == game_command[3]:
        os.system("cls")
        print(game_titele)
        game_statis_read()
        return entry
    elif not entry:
        print(game_messages["E12"])
        return entry
    else:
        return entry


def input_validation_horizontal():
    """ funkcja odpowiedzialna za weryfikację pozycjonowania statku"""
    statu = True
    while  statu == True:
        try:
            shi_d = input_validation_game_option(input(f'{game_messages["I13"]} -> '))
            if shi_d.upper() not in ship_direction:
                print(game_messages["E9"])
                statu == True
            else:
                statu == False
                return shi_d.upper()
        except ValueError:
                print(game_messages["E11"])
                statu == True


def input_validation_coulumn(alphabet):
    """ funkcja odpowiedzialna za weryfikację czy włąściwie wprowadzono literę oznaczjącą kolumny"""
    statu = True
    while  statu == True:
        try:
            col_s = input_validation_game_option(input(f'Write leter from A to {alphabet[-1]} column - ship start form here -> '))
            if col_s.upper() not in alphabet:
                print(f'{game_messages["E4"]} {alphabet[-1]}')
                statu == True
            else:
                statu == False
                col_s = int(alphabet.find(col_s.upper()))
                return col_s
        except ValueError:
                print(game_messages["E13"])
                statu == True


def input_validation_length(ship_size):
    """ funkcja odpowiedzialna za weryfikację czy włąściwie wprowadzono wartość długości statku"""
    statu = True
    while  statu == True:
        try:
            len_g = input_validation_game_option(input(f'Write ship size 1 to {ship_size} lengh -> '))
            if int(len_g) not in range(1,ship_size+1):
                print(f'{game_messages["E5"]} {ship_size}')
                statu == True
            else:
                statu == False
                return int(len_g)
        except ValueError:
                print(f'{game_messages["E10"]} please')
                statu == True


def input_validation_row(board_size):
    """ funkcja odpowiedzialna za weryfikację czy właściwie numer wiersza"""
    statu = True
    while  statu == True:
        try:
            row_s  = input_validation_game_option(input(f'Write number from 1 to {board_size} row - ship start form here -> '))
            if int(row_s) not in range(1, board_size + 1):
                print(f'{game_messages["E5"]} {board_size}')
                statu == True
            else:
                statu == False
                return int(row_s)
        except ValueError:
                print(f'{game_messages["E11"]} please\n')
                statu == True


def input_validation_board_size():
    """ funkcja odpowiedzialna za weryfikację czy wybraono wielkość planszy - ograniczenie do 26"""
    statu = True
    while  statu == True:
        try:
            board_size  = input_validation_game_option(input(f'{game_messages["I5"]} -> '))
            if int(board_size) not in range(5, board_maximal_rang+1):
                print(game_messages["E1"])
                statu == True
            else:
                statu == False
                return int(board_size)
        except ValueError:
                print(f'{game_messages["E16"]} please\n')
                statu == True


def input_validation_game_who_play():
    """ funkcja odpowiedzialna za weryfikację czy wybrano poprawnie z listy możliwości rozgrywek"""
    statu = True
    while  statu == True:
        try:
            who_play  = input_validation_game_option(input(f'{game_messages["I7"]} -> '))
            if int(who_play) not in game_who_play.keys():
                print(game_messages["E17"])
                statu == True
            else:
                statu == False
                return int(who_play)
        except ValueError:
                print(f'{game_messages["E18"]} please\n')
                statu == True


def input_validation_game_diff():
    """ funkcja odpowiedzialna za weryfikację czy wybrano poprawnie z listy trudności gry"""
    statu = True
    while  statu == True:
        try:
            game_level  = input_validation_game_option(input(f'{game_messages["I10"]} -> '))
            if int(game_level) not in game_difficult.keys():
                print(game_messages["E19"])
                statu == True
            else:
                statu == False
                return int(game_level)
        except ValueError:
                print(f'{game_messages["E18"]} please\n')
                statu == True


def input_validation_player_name(name):
    """ funkcja odpowiedzialna za wprowadzenie danej anonymus jak nic nie zostanie wprowadzone
        to możnabyłoby zoptymalizować poprze wprowadzenie parametru name = 'ANONYMUS' ale z póżno by to zmieniać
    """
    if name != "quit":
        if not name:
            name = "ANONYMUS"
            return name.upper()
        else:
            return name.upper()
    else:
        os.system("cls")
        print(game_titele)
        game_statis_read()
        print(game_messages["S12"])
        exit()
    