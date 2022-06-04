import os
import random
import time
import sys
from datetime import date
from datetime import datetime

from time_game import day_time
from screen_deposit import game_titele, game_help, game_over
from messages import game_messages
from validation_input import input_validation_horizontal, input_validation_coulumn, input_validation_row, input_validation_length, input_validation_board_size, input_validation_game_who_play, input_validation_game_diff, input_validation_player_name
from validation_win import  validation_shot_basic
from parematers import alphabet_max, players_availlable, ship_direction,board_size_sep, game_command, game_who_play, game_difficult, board_signes, game_colours
from game_stat import game_statis_append, game_statis_read, game_see_choice
from shooting import print_boards
from final_massages import print_win_boards

'''
This module is used for:
def display_board   print the board
def status_empty    check availlable moves 
def status          check winning status
'''

#parametry globalne
board_size = 0
lives_max_number = 0
board_size_len = 0
ship_size = 0
alphabet = ""
bullets = 0
battle_see_name = ""
game_level = ""
player_1 ={"name":["Under Construction","ANONYMUS"], "ship_location":[],"bullets":[0,0],"units":0,"ship_no":[0,0],"board":[[[]],[[]]]}
player_2 ={"name":["Under Construction","ANONYMUS"], "ship_location":[],"bullets":[0,0],"units":0,"ship_no":[0,0],"board":[[[]],[[]]]}
player_current = {}
game_start = None
game_end = None



def board_empty(board_size, board):
    """ General finction creation of empty board"""
    for board_row in range(board_size):
        board.append([board_signes["empty"]] * board_size)
    for i in alphabet:
        board[0].append(i)
    return board


def print_board(player):
    """ General finction to print board and title"""
    if player == player_1:
        board = player_1["board"][0]
    else:
        board = player_2["board"][0]
    print(game_titele)
    day_time()
    print('THE BATTLEFILED\n')
    for x, y in enumerate(board):
        if x == 0:
            print(game_colours["MESSE_STA"]+f'{"COLUMN"}{" " * (board_size_len - len(str(x)))} | {board_size_sep.join(y)}'+game_colours["MESSE_END"])
            print(f'{"-" * 10}{"-" * (board_size * 2)}')
        else:
            print(game_colours["MESSE_STA"]+f'ROW  {x}{" " * (board_size_len - len(str(x)))} | {board_size_sep.join(y)}'+game_colours["MESSE_END"])
    print(f'{"-" * 10}{"-" * (board_size * 2)}\n')
    return player


def game_start():
    global game_start
    global game_end
    # get_game_statistic()
    os.system("cls")
    game_start = time.time()
    try:
        if len(sys.argv) <= 1:
            game_parametrization()
            # game_initiation()
        else:
            if sys.argv[1] == game_command[0]: # agrv - to ważna komenda - anmienia linie poleceń na listę, którą można ITEROWAĆ
                game_parametrization()
            elif sys.argv[1] == game_command[2]:
                print(game_titele)
                day_time()
                print("-" * 126)
                print(game_help)
                print("-" * 126)
                game_end = time.time()
            elif sys.argv[1] == game_command[3]:
                print(game_titele)
                day_time()
                print("-" * 126)
                game_statis_read()
                print("-" * 126)
                game_end = time.time()
            else:
                os.system("cls")
                print(game_titele)
                day_time()
                game_parametrization()
    except ValueError:
            os.system("cls")
            game_parametrization()
            


def game_parametrization():
    global board_size_len
    global ship_size
    global lives_max_number
    global alphabet
    global board_size
    global player_1
    global player_2
    global player_current
    global bullets
    global battle_see_name
    global game_level 

    '''This function initiate the game parameter'''
    player_1 ={"name":["Under Construction","ANONYMUS"], "ship_location":[],"bullets":[0,0],"units":0,"ship_no":[0,0],"board":[[[]],[[]]]}
    player_2 ={"name":["Under Construction","ANONYMUS"], "ship_location":[],"bullets":[0,0],"units":0,"ship_no":[0,0],"board":[[[]],[[]]]}
    print(f'{game_titele}')
    day_time()
    battle_see_name = game_see_choice()
    print(f'!!! {game_messages["I1"]} !!!') 
    operator_name = input_validation_player_name(input(f'\n{game_messages["I2"]} > '))
    print(f'\n\t{game_messages["S19"]} {operator_name}\n')
    print(f'!!! {game_messages["I4"]} !!!')
    #beginning game parameters 
    board_size = input_validation_board_size()
    alphabet = alphabet_max[0:board_size]
    board_size_len = len(str(board_size))
    ship_size = board_size - 2 #the game calculate max ship size base on board dimension - less by 2
    lives_max_number = int(((board_size**2)*0.12)+1)  #the game calculate max unit for ship construction limit to 12% area board
    print(f'\n{game_messages["S20"]}\n')
    who_play = input_validation_game_who_play()#the game parameters determine who play the game
    print(f'\n\t{game_messages["S21"]} {game_who_play[who_play][0]} vs {game_who_play[who_play][1]}\n')
    game_level = input_validation_game_diff()
    print(f'\n\t{game_messages["S21"]} {game_difficult[game_level][0]}')
    bullets = int((board_size**2 * game_difficult[game_level][1]/100))
    print(f'\t{game_messages["S22"]} {bullets}\n')
    player_1["bullets"]=[bullets,0]
    player_2["bullets"]=[bullets,0]
    player_1["units"]=lives_max_number
    player_2["units"]=lives_max_number
    board_empty(board_size, player_1["board"][0])
    board_empty(board_size, player_1["board"][1])
    board_empty(board_size, player_2["board"][0])
    board_empty(board_size, player_2["board"][1])
    player_current = player_1

    board_players(who_play, operator_name, player_1, player_2, game_level)

    game_shooting_phase(board_size, player_1, player_2)


def board_players(who_play, operator_name, player_1, player_2, game_level):
    global player_current
    if who_play == 1:
        player_1["name"]=[players_availlable[1][0],operator_name.upper()]
        opponent_name = input_validation_player_name(input(f'{game_messages["I3"]} > '))
        print(f'\n\t{game_messages["S19"]} {opponent_name}\n')
        human_board(player_1)
        player_2["name"]=[players_availlable[1][0],opponent_name.upper()]
        human_board(player_2)
    elif who_play == 2:
        player_1["name"]=[players_availlable[1][0],operator_name.upper()]
        human_board(player_1)
        player_2["name"]=[players_availlable[2][0],players_availlable[2][1]]
        comp_board(player_2)
    elif who_play == 3:
        player_1["name"]=[players_availlable[2][0],players_availlable[2][1]]
        comp_board(player_1)
        player_2["name"]=[players_availlable[1][0],operator_name.upper()]
        human_board(player_2)
    else:
        player_1["name"]=[players_availlable[2][0],operator_name.upper()]
        comp_board(player_1)
        player_2["name"]=[players_availlable[2][0],players_availlable[2][1]]
        comp_board(player_2)
    
    game_statis_append(who_play,game_level,board_size)
    print_table(game_level)


def print_table(game_level):
    """
    Parametrization table
    """
    names_1_len = len(player_1["name"][1]) + len(player_1["name"][0])
    names_2_len = len(player_2["name"][1]) + len(player_2["name"][0])
    player_1_id1 = player_1["name"][1]
    player_1_id2 = player_1["name"][0]
    player_2_id1 = player_2["name"][1]
    player_2_id2 = player_2["name"][0]
    bullets = player_1["bullets"][0]
    difflevel = game_difficult[game_level][0]
    see_size = board_size**2
    if names_1_len < 25 and names_2_len < 25:
        max_len_key = 25
    elif names_1_len >= names_2_len:
        max_len_key = names_1_len
    else:
        max_len_key = names_2_len

    os.system("cls")
    day_time()
    print(f'\n{game_messages["S23"]}\n')
    print('-' * ((max_len_key)*2+3))
    print(f'{"Player 1" :<{max_len_key}} | {player_1_id1  :^{max_len_key}}')
    print(f'{"  Type" :<{max_len_key}} | {player_1_id2  :^{max_len_key}}')
    print('-' * ((max_len_key)*2+3))
    print(f'{"Player 2" :<{max_len_key}} | {player_2_id1  :^{max_len_key}}')
    print(f'{"  Type" :<{max_len_key}} | {player_2_id2  :^{max_len_key}}')
    print('-' * ((max_len_key)*2+3))
    print(f'{"Game level" :<{max_len_key}} | {difflevel :^{max_len_key}}')
    print('-' * ((max_len_key)*2+3))
    print(f'{"See name " :<{max_len_key}} | {battle_see_name :^{max_len_key}}')
    print('-' * ((max_len_key)*2+3))
    print(f'{"Grid are " :<{max_len_key}} | {see_size :^{max_len_key}}')
    print('-' * ((max_len_key)*2+3))
    print(f'{"Missails availlable" :<{max_len_key}} | {bullets :^{max_len_key}}')
    print('-' * ((max_len_key)*2+3))
    print(f'\n{game_messages["S24"]}')
    print(f'\n{game_messages["I14"]}')
    print_boards(board_size_len, board_size, player_1, player_2)
    time.sleep(5)


def human_board(player):
    global player_current
    """Funkcja odpowiadająca z ustawianie statków przez gracza"""
    global ship_size
    while player["units"] > 0:
        os.system("cls")
        print_board(player)
        #komunikaty 
        print(f'{game_messages["S15"]} for {player["name"][0]} {player["name"][1]}')
        print(f'{game_messages["S14"]}{len(player["ship_location"])} ships')
        print(f'{game_messages["S13"]}{player["units"]} units')
        print(f'{game_messages["S17"]} {ship_size}')
        entry_status = True
        
        while entry_status == True:
            #komunikaty 
            
            print(f'{game_messages["S15"]} for {player["name"][0]} {player["name"][1]}')
            print(f'{game_messages["S18"]} {player["units"]}')
            
            #sprawdzenie poprawności z modułu walidacyjnego
            shi_d = input_validation_horizontal()       
            col_s = input_validation_coulumn(alphabet)
            row_s = input_validation_row(board_size)
            len_g = input_validation_length(ship_size)

            #sprawdzenie czy mamy odpowiednią ilość części na zbudowanie statku
            if player["units"] - len_g < 0:
                print(f'{game_messages["E15"]} {player["units"]}')
                time.sleep(2)
                entry_status = False
            else:
                if ship_placement(shi_d, col_s, row_s, len_g, player):
                    player["units"] -= len_g
                    if player["units"] > 0:
                        os.system("cls")
                        print_board(player)
                        print(f'{game_messages["S7"]}')
                        time.sleep(2)
                        entry_status = True
                    else:
                        os.system("cls")
                        print_board(player)
                        player["ship_no"]=[len(player["ship_location"]),len(player["ship_location"])]
                        print(game_messages["S10"])
                        time.sleep(2)
                        entry_status = False
                else:
                    entry_status = True


def comp_board(player):
    """Funkcja odpowiadająca z ustawianie statków przez gracza, którym jest komputer """

    while player["units"] > 0:
        
        entry_status = True
        
        while entry_status == True:
            shi_d = random.choice(ship_direction)                       #losowe wybranie ze słownika kierunku pozycjonowania statku
            col_s = random.randint(0, board_size - 1)                   #losowe wybranie kolumny od którego statek się zaczyna (pomijamy alfabet bo komuter daje sobie radę z cyframi) 
            row_s = random.randint(1, board_size)                       #losowe wybranie wiersza od którego statek się zaczyna 
            len_g = random.randint(1, ship_size)                        #losowe wybranie długości statku z ustalonego zakresu 1 parametry 
            
            #sprawdzenie czy mamy odpowiednią ilość części na zbudowanie statku
            if player["units"] - len_g < 0:                     #warunek sprawdzający ile części gracz ma na konstruowanie statku
                entry_status = False
            else:
                if ship_placement(shi_d, col_s, row_s, len_g, player):  #odwołanie się do walidacji pozycjonowania
                    player["units"] -= len_g                            #skoro warunek został poprawnie speniopny to odejmuje mu częsci z dostępnych graczowi
                    if player["units"] > 0:                           
                        os.system("cls")
                        print_board(player)         
                        print(game_messages["S7"])                      #to by fajnie było widać, że proces konstruowania statku został ukończony
                        time.sleep(1)
                        entry_status = True
                    else:
                        os.system("cls")
                        print_board(player)
                        print(game_messages["S10"])                         #a skoro już nie ma unitów to nie doś, ze proces kostruowania statku się zakończył ale równjież budowy całej
                        player["ship_no"]=[len(player["ship_location"]),len(player["ship_location"])]   #ilość zbodowanych statków
                        time.sleep(2)
                        entry_status = False
                entry_status = True
    print(game_messages["S16"])

    
def ship_placement(ship_direction, col_start, row_start, length, player):
    global player_current
    """Funkcja sprawdzająca umiejscawianie staku - cześć odpowiedzilna za sprawdzenie czy długość statku mieści się w zakresie"""
    board_size = len(player["board"][0]) - 1            #wyliczenie zakresu
    if ship_direction == "H":                           #sprawdzenie czy statek jest umieszczony poziomo
        if col_start + length - 1 > board_size:
            if player["name"][0] == "Computer":         #sprawdzenie gracza - chodzi o komunikat, dla komputera nie wyświetlamy
                return False
            else:
                print(game_messages["E8"])              #komunikat błędu - lista w messeges.py
                return False
        else:
            col_end = col_start + length - 1            #obliczenie zakresów (kolumna końcowa + długość statku - 1)
            row_end = row_start                         #skoro poziomo więc wiersz nie może być inny
    else:                                               #skoro ni poziomo więc statek jest pionowo
        if row_start + length -1 > board_size:
            if player["name"][0] == "Computer":         #sprawdzenie gracza - chodzi o komunikat, dla komputera nie wyświetlamy
                return False
            else:
                print(game_messages["E8"])              #komunikat błędu - lista w messeges.py
                return False
        else:
            row_end = row_start + length - 1            #obliczenie zakresów (wiersz końcowy + długość statku - 1)
            col_end = col_start                         #skoro pionowo więc kolumny nie mogą być inne
            
    return ship_placement_check(col_start, row_start, col_end, row_end, player, length)


def ship_placement_check(col_start, row_start, col_end, row_end, player, length):
    global player_current
    """Funkcja sprawdzająca umiejscawianie staku - cześć odpowiedzilna za sprawdzenie czy długość statku mieści się w zakresie"""
    global board_size
    #ważny element = jak zprawdzać to trzeba wiedzieć kogo?
    if player == player_1:
        board = player_1["board"][0]
    else:
        board = player_2["board"][0]
    entry_status = True
    
    try:
        for r in range(row_start, row_end + 1):
            for c in range(col_start, col_end + 1):
                if board[r][c] != board_signes['empty']:
                    if player["name"][0] == "Computer":     #sprawdzenie gracza - chodzi o komunikat, dla komputera nie wyświetlam
                        entry_status = False
                        break
                    else:
                        print(game_messages["E14"])         #komunikat błędu - lista w messeges.py
                        entry_status = False
                        break
        if entry_status:                                    #skoro błedu nie zwrócił podczas sprawdzenie całej listy
            player["ship_location"].append([col_start, row_start, col_end, row_end,[length,length]]) #uzupełniam listę statków w słownuiku gracza
            for r in range(row_start, row_end + 1):         #uzupełniam znak statku - u nas można go łatwo zmienić w parametrach gry
                for c in range(col_start, col_end + 1):
                    board[r][c] = board_signes['ship']      #wstawiamy odpowiedni znak w tabeli gracza
            border_fulfilment(col_start, row_start, col_end, row_end, board) #statki mają się nie stykać więc
            entry_status = True
            return entry_status
    except IndexError:
        entry_status = False
        return entry_status


def border_fulfilment(col_start, row_start, col_end, row_end, board):
    global player_current
    global board_size
    """Funkcja uzupełniająca bufory - staki nie moga się stykać"""
    if col_start - 1 < 0:                                   #to istotne zabiegi o jak nie to zakres będzie niepoprawny
        col_start = 0
    else:
        col_start = col_start - 1
    if row_start - 1 < 1:
        row_start = 1
    else:
        row_start = row_start - 1
    
    for r in range(row_start, row_end + 2):                 #ustalony zakres
        for c in range(col_start, col_end + 2):
            try:
                if board[r][c] == board_signes['empty']:
                    board[r][c] = board_signes['separation']
            except IndexError:
                continue


def change_player():
    global player_current
    if player_current == player_1:
        player_current = player_2
        return player_current
    else:
        player_current = player_1
        return player_current
    

def game_shooting_phase(board_size, player_1, player_2):
    global lives_max_number
    global player_current
    game_status = True
    while game_status == True:

        os.system("cls")
        print(game_titele)
        day_time()
        print_boards(board_size_len, board_size, player_1, player_2)
        
        if player_current == player_1:
            player = player_1
            competitor = player_2
        
        else:
            player = player_2
            competitor = player_1
        
        print(f'\n{game_messages["S31"]} -  {player["name"][1]} shoot')
        
        if player['name'][0] == players_availlable[2][0]:
            
            comp_choice = True
            
            while comp_choice == True:

                # --------------------------------------------------------------------------------------------------------------------------------------------------------------------
                # tutaj zaczyna się BI dla komputera!!
                # --------------------------------------------------------------------------------------------------------------------------------------------------------------------

                if game_level == 3:
                    
                    status_target = True
                    
                    try_list = []
                    
                    for r in range(1, board_size + 1):
                        for c in range(0, board_size):
                            if player["board"][1][r][c] == board_signes["hit"]:
                                try_list.append([r,c])                              #lista znalezionych trafień
                                status_target = False

                    if status_target:
                                                                       #jeżeli lista znalezionych trafień jest pusta
                        comp_separation = True
                        while comp_separation is True:

                            c = random.randint(0, board_size - 1)                   
                            r = random.randint(1, board_size)

                            if player["board"][1][r][c] == board_signes["separation"]:
                                comp_separation = True
                            else:
                                comp_separation = False

                        comp_choice = False
                    
                    else:
                        #jeżeli znalazł trafinie

                        status2 = False #statusy poszukiwań nie ma sensu aby sprawdzał warunek "true" jeżeli w kolejnym etapie wykonanie procedury może być zbędne
                        status3 = False #statusy poszukiwań nie ma sensu aby sprawdzał warunek "true" jeżeli w kolejnym etapie wykonanie procedury może być zbędne

                        r_target = try_list[0][0] - 1 #sprawdza powyżej pierwszego elementu z listy trafień
                        c_target = try_list[0][1]

                        try:
                            if try_list[0][1] - try_list[-1][1] == 0:
                                if player["board"][1][r_target][c_target] == board_signes["empty"]:
                                    r = r_target
                                    c = c_target
                                    status1 = False
                                    comp_choice = False
                                    break
                                else:
                                    status1 = True
                            else:
                                status1 = True                        
                        except IndexError:
                            status1 = True                        
                        
                        if status1: #jeżeli powyżej nie znalazł sprawdza poniżej
    
                            try:
                                r_target = try_list[-1][0] + 1  #sprawdza poniżej ostatniego elementu z listy trafień
                                c_target = try_list[0][1]                             

                                if try_list[0][1] - try_list[-1][1] == 0:
                                    if player["board"][1][r_target][c_target] == board_signes["empty"]:
                                        r = r_target
                                        c = c_target                            
                                        status2 = False
                                        comp_choice = False
                                    else:
                                        status2 = True
                                else:
                                    status2 = True
                            except IndexError:
                                status2 = True

                        if status2: #jeżeli powyżej i poniżej nie znalazł sprawdza po lewej

                            status3 = True
                            
                            try:
                                r_target = try_list[0][0]
                                c_target = try_list[0][1] - 1 #sprawdza z lewej od pierwszego elementu z listy trafień

                                if try_list[0][0] - try_list[-1][0] == 0:
                                    if player["board"][1][r_target][c_target] == board_signes["empty"]:
                                        r = r_target
                                        c = c_target
                                        status3 = False
                                        comp_choice = False
                                    else:
                                        status3 = True
                                else:
                                        status3 = True
                            except IndexError:
                                status3 = True
                        
                        #jeżeli powyżej i poniżej i z lewej nie znalazł sprawdza po prawej
                        if status3:
                            if try_list[0][0] - try_list[-1][0] == 0:
                                r_target = try_list[0][0]
                                c_target = try_list[-1][1] + 1 #sprawdza poniżej ostatniego elementu z listy trafień
                                if player["board"][1][r_target][c_target] == board_signes["empty"]:
                                    r = r_target
                                    c = c_target
                                    comp_choice = False
                                else:
                                    comp_choice = False
                            else:
                                comp_choice = False

                else:
                    c = random.randint(0, board_size - 1)
                    r = random.randint(1, board_size)
                    comp_choice = False

                #jeżeli gra typu EASY to komputer strzela gdzie popadnie i ma sklerozę bo nie pamięta gdzie strzelał wcześniej
                
                if game_level == 1: 
                    player["bullets"][0] -= 1
                    player["bullets"][1] += 1
                    comp_choice = False

                #w postałych przypadkac strzela gdzie popadnie ale nie ma problemu z pamięcią (na BI nie starczyło nam czasu!!)                
                else:

                    if competitor["board"][0][r][c] == board_signes["missed"] or competitor["board"][0][r][c] == board_signes["hit"] or competitor["board"][0][r][c] == board_signes["sunk"]:
                        comp_choice = False
                    else:
                        player["bullets"][0] -= 1
                        player["bullets"][1] += 1
                        comp_choice = False
        else:
            c = input_validation_coulumn(alphabet)
            r = input_validation_row(board_size)
            player["bullets"][0] -= 1
            player["bullets"][1] += 1
        validation_shot_basic(player, competitor, c, r, game_level)

        if player["bullets"][0] > 0 and competitor["ship_no"][1] > 0:

            change_player()
            game_status = True
        
        else:

            if player["bullets"][0] == 0:
                os.system("cls")
                print(game_titele)
                day_time()
                print(game_over)
                print(f'{"-" * 10}{"-" * (board_size * 2)}')
                print(f'{game_messages["S29"]} {battle_see_name}')
                print(f'{game_messages["S30"]} {game_difficult[game_level][0]}')
                print(f'{game_messages["S8"]} {competitor["name"][0]} {competitor["name"][1]} {game_messages["S27"]}\n')
                print_win_boards(board_size_len, board_size, player, competitor)
                print(f'{"-" * 10}{"-" * (board_size * 2)}')
                game_status = False
            
            elif competitor["ship_no"][1] == 0:
                os.system("cls")
                print(game_titele)
                day_time()
                print(game_over)
                print(f'{"-" * 10}{"-" * (board_size * 2)}')
                print(f'{game_messages["S29"]} {battle_see_name}')
                print(f'{game_messages["S30"]} {game_difficult[game_level][0]}')
                print(f'{game_messages["S8"]} {player["name"][0]} {player["name"][1]} {game_messages["S28"]}\n')
                print_win_boards(board_size_len, board_size, player, competitor)
                print(f'{"-" * 10}{"-" * (board_size * 2)}')
                game_status = False
    
    game_end = time.time()
    time_use = (int(game_end - game_start))
    
    print(f'\n{player_2["name"][1]} - All in all, you spent playing {time_use} seouns\n')
    again = input(f'{game_messages["E20"]} ')

    if again.lower() == "y":
        os.system("cls")
        game_parametrization()
    
    else:
        os.system("cls")
        print(game_titele)
        day_time()
        game_statis_read()
        print(game_messages["S12"])
        exit()
                
if __name__ == '__main__':
    game_start()