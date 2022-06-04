import time
from validation_input import input_validation_coulumn, input_validation_row 
from parematers import alphabet_max, players_availlable, ship_direction,board_size_sep, board_maximal_rang, game_command, game_who_play, game_difficult, board_signes, game_colours
from messages import game_messages
from shooting import status_bar


def print_win_boards(board_size_len, board_size, player, competitor):
    print(game_colours["MESSE_STA"]+f"{player['name'][0]} {player['name'][1]} armament and ship (status bar), and below a ships location map"+game_colours["MESSE_END"])
    status_bar(player, board_size)
    for x, y in enumerate(player["board"][0]):
        if x == 0:
            print(game_colours["MESSE_STA"]+f'{"COLUMN"}{" " * (board_size_len - len(str(x)))} | {board_size_sep.join(y)}'+game_colours["MESSE_END"])
            print(f'{"-" * 10}{"-" * (board_size * 2)}')
        else:
            print(game_colours["MESSE_STA"]+f'ROW  {x}{" " * (board_size_len - len(str(x)))} | {board_size_sep.join(y)}'+game_colours["MESSE_END"])
    print(f'{"-" * 10}{"-" * (board_size * 2)}\n')
    print(game_colours["MESSE_STA"]+f"{competitor['name'][0]} {competitor['name'][1]} armament and ship (status bar), and below a ships location map"+game_colours["MESSE_END"])
    status_bar(competitor, board_size)
    for x, y in enumerate(competitor["board"][0]):
        if x == 0:
            print(game_colours["MESSE_STA"]+f'{"COLUMN"}{" " * (board_size_len - len(str(x)))} | {board_size_sep.join(y)}'+game_colours["MESSE_END"])
            print(f'{"-" * 10}{"-" * (board_size * 2)}')
        else:
            print(game_colours["MESSE_STA"]+f'ROW  {x}{" " * (board_size_len - len(str(x)))} | {board_size_sep.join(y)}'+game_colours["MESSE_END"])
    print(f'{"-" * 10}{"-" * (board_size * 2)}\n')
