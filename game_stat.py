import time
import random
import pandas as pd
from csv import writer
from parematers import game_difficult, game_who_play
from screen_deposit import game_titele
from messages import game_messages
"""
We try to learn and last lesson was related to file managment. Even the game instuction does not requiers we add this
to practice as much as Possible and utilise CodeCool to extreme.

The file name is game_statistic.txt
3 data is coleected while parametrization proces is completed
each line - mode, dificulty level, board size

where
1- Player mode
2- Dificulty level
3- Board size
"""

def game_statis_read():
    with open("statistic.csv") as gs_file:
        df = pd.read_csv(gs_file)
        count_row = df.shape[0] #gives number of rows
        count_col = df.shape[1] #gives number of coulumns
        print(f'\n\t{game_messages["S25"]}\n')
        print(f'| {"Game Type Mode" :^20} | {"Games" :^8} | {"Ave grid"  :^8} |')
        for i in game_who_play.keys():
            len_by_gm_mode = len(df[(df["Game Mode"] == i)])
            sum_of_see = df.loc[df["Game Mode"] == i,"Board Size"].sum()
            if len_by_gm_mode ==0:
                average_see ==0
            else:
                average_see = int(sum_of_see / len_by_gm_mode)
                text_marge = f'{game_who_play[i][0]} vs {game_who_play[i][1]}'
                print('-' * 46)
                print(f'| {text_marge :<20} | {len_by_gm_mode :>8} | {average_see  :>8} |')
        for j in game_difficult.keys():
            len_by_df_mode = len(df[(df["Difficulty Mode"] == j)])
            sum_of_see = df.loc[df["Difficulty Mode"] == j,"Board Size"].sum()
            if len_by_df_mode ==0:
                average_see ==0
            else:
                average_see = int(sum_of_see / len_by_df_mode)
                print('-' * 46)
                print(f'| {game_difficult[j][0] :<20} | {len_by_df_mode :>8} | {average_see :>8} |')
        print(f"{'-' * 46}\n")


def game_statis_append(game_mode,difficulty_mode,board_size):
    game_data_for_statistic=[game_mode,difficulty_mode,board_size]
    with open("statistic.csv", 'a',  newline='') as gs_file:
        list_obj_to_add=writer(gs_file)
        list_obj_to_add.writerow(game_data_for_statistic)


def game_see_choice():
    with open("see_list.txt") as gs_file:
        choice_see = random.randint(0,75)
        for pos, l_num in enumerate(gs_file):
            if pos == choice_see:
                sen_name = l_num.rstrip('\n')
                return sen_name
