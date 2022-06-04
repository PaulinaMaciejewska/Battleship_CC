import os
import time
from messages import game_messages
from parematers import ship_direction, board_maximal_rang, game_who_play, game_difficult, game_colours, board_signes, game_command, players_availlable
from screen_deposit import game_help, game_titele

""" moduł sprawdzający poprawniść wpisania danych przez gracza"""

def validation_shot_basic(player, competitor, c, r, game_level):
    """ funkcja sprawdzająca strzał"""
    if  competitor["board"][0][r][c] == board_signes["ship"]:   #sprawdzenie czy tam nie ma celu
        competitor["board"][0][r][c] = board_signes["hit"]      #wpisuje odpowiedni znak trafienia
        player["board"][1][r][c] = board_signes["hit"]
        competitor["units"] -= 1
        validation_ships_destroy(player, competitor, c, r, game_level)      #sprawdza kondycje statku
        return player, competitor, c, r
    elif competitor["board"][0][r][c] == board_signes["separation"] or competitor["board"][0][r][c] == board_signes["empty"] and player["board"][1][r][c] != board_signes["separation"] : #jeżeli nie to sprawdza czy pole jest dostępne
        competitor["board"][0][r][c] = board_signes["missed"]   #jeżeli tak to wpisuje znak chybienia
        player["board"][1][r][c] = board_signes["missed"]       #jeżeli tak to wpisuje znak chybienia
        if player["name"][0] != players_availlable[2][0]:
            print(game_messages["S2"])                          #wypisuje komunikat
            time.sleep(2)
    else:
        if player["name"][0] != players_availlable[2][0]:
            print(game_messages["S1"])
            time.sleep(2)


def validation_ships_destroy(player, competitor, c, r, game_level):
    """ 
    funkcja sprawdzająca zatopienie statku oraz zamienioająca jego oznaczenie na sunk
    dodatkowo uzupełnia buforowanie miedzy statkami tak by nie strzelać w z góry zablokowane miejsca,
    ta opcja działa jednynie w wariancie EASY dla Hyuman i od opcji Easy dla Computera
    """
    for ships in competitor["ship_location"]:
        iunit_r_s = ships[1]
        iunit_c_s = ships[0]
        iunit_r_e = ships[3]
        iunit_c_e = ships[2]

        if r in range(iunit_r_s, iunit_r_e + 1) and c in range(iunit_c_s, iunit_c_e + 1):
            if ships[4][1] == 1:                    # jeżeli to ostatni element statku
                ships[4][1] -= 1
                if iunit_c_s - 1 < 0:               # to istotne zabiegi o jak nie to zakres będzie niepoprawn
                    iunit_c_s = 0
                else:
                    iunit_c_s = iunit_c_s
                if iunit_r_s - 1 < 1:
                    iunit_r_s = 1
                else:
                    iunit_r_s = iunit_r_s
                try:
                    for unit_r in range(iunit_r_s, iunit_r_e + 1):
                        for unit_c in range(iunit_c_s, iunit_c_e + 1):
                            competitor['board'][0][unit_r][unit_c] = board_signes['sunk']   # zamienia wszystkie jego znaki na na "sunk"
                            player['board'][1][unit_r][unit_c] = board_signes['sunk']       # zamienia wszystkie jego znaki na na "sunk"
                    if player["name"][0] != players_availlable[2][0]:
                        print(game_messages["S4"])
                        time.sleep(2)
                        competitor["ship_no"][1] -= 1
                    else:
                        competitor["ship_no"][1] -= 1
                except IndexError:
                    if player["name"][0] != players_availlable[2][0]:
                        time.sleep(2)
                        continue
                    else:
                        continue

                #boforowanie wspomagające - dziła w opcji EASY dla Human oraz dla COMP tylko level MID I HARD

                if game_level == 3 and player["name"][0] == players_availlable[2][0] or game_level != 3 and player["name"][0] != players_availlable[2][0]:
                    if iunit_c_s - 1 < 0:               # to istotne zabiegi o jak nie to zakres będzie niepoprawn
                        iunit_c_s = 0
                    else:
                        iunit_c_s = iunit_c_s-1
                    if iunit_r_s - 1 < 1:
                        iunit_r_s = 1
                    else:
                        iunit_r_s = iunit_r_s-1
                    for r in range(iunit_r_s, iunit_r_e + 2):     #ustalony zakres
                        for c in range(iunit_c_s, iunit_c_e + 2):
                            try:
                                if player['board'][1][r][c] == board_signes['empty']:
                                    player['board'][1][r][c] = board_signes['separation']
                            except IndexError:
                                continue

            else:
                if player["name"][0] != players_availlable[2][0]:
                    ships[4][1] -= 1
                    time.sleep(2)
                    print(game_messages["S2"])
                else:
                    ships[4][1] -= 1
                    