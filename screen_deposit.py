import os
from parematers import game_colours

game_help =(game_colours["HELP_SCREEN_START"]+
    '''
    BATTLESHIP by Paulina & Arek
    _______________________________________________________________________________________________________________________________________________
    Battleship (also known as Battleships or Sea Battle[1]) is a strategy type guessing game for two players. 
    It is played on ruled grids (paper or board) on which each player's fleet of warships are marked. 
    The locations of the fleets are concealed from the other player. 
    Players alternate turns calling "shots" at the other player's ships, and the objective of the game is to destroy the opposing player's fleet.

    Battleship is known worldwide as a pencil and paper game which dates from World War I.
    It was published by various companies as a pad-and-pencil game in the 1930s and was released as a plastic board game by Milton Bradley in 1967. 
    The game has spawned electronic versions, video games, smart device apps and a film.
    _______________________________________________________________________________________________________________________________________________
    Let puch BATTLESHIP to next level
    
    4 steps to start the GAME A, B, C, D
    
    A First = you will be asked for board size - number from 5 to 26
    
    B Second = you have to tell who plays the game:
        1 - Human    vs  Human
        2 - Human    vs  Computer
        3 - Computer vs  Human
        4 - Computer vs  Computer

    C Next = you have to assign difficulty mode (it determines some limits and give some instruction for computer)
        1- easy - 2 times board area - hope is enough (computer do not remember its moves in case you play against him)
        2- mid - number of missiles is reduced to 100% of board area - (computer remember its moves and do not shoot serrounding sunk place)
        3- hard - number of misals is reduced to 75% of free availlable spaces

    D Finally if your choice in section B was 1, 2 or 3 you will be aske to place your ship on the board

    You are ready to play

    You can use terminal parameters:
        1- help - the game help will be displayed
        2- start - the game statistic will be displayed
        3- play - you start

    Game is finishe when:
    SHIP SUNK       winner is the one who first sunk all opponent's ships
        or 
    BULLETS LUCK    the losser is who first run out of bullets

    You always have the option to stop application by entering the word quit.
                                                            Please note the see name in the end are real name and print to remind some geography.
    _______________________________________________________________________________________________________________________________________________
    '''
    +game_colours["HELP_SCREEN_END"])
game_titele = (game_colours["TITEL_S"]+
"""                                                                                   
          ########   #########  #########  #########  ###        #########  #########  ###   ###  ###  #########  COLUMN | A B C D E
         #########  #########  #########  #########  ###        #########  #########  ###   ###  ###  #########   -------------------
        ###    ##  ###   ###     ###        ###     ###        ###        ###        ###   ###  ###  ###   ###    ROW  1 | . . . . .
       ########   #########     ###        ###     ###        #########  #########  #########  ###  #########     ROW  2 | . O . O .
      ###    ##  ###   ###     ###        ###     ###        ###              ###  ###   ###  ###  ###            ROW  3 | . . # . .
     #########  ###   ###     ###        ###     #########  #########  #########  ###   ###  ###  ###             ROW  4 | . X X X .
    ########   ###   ###     ###        ###     #########  #########  #########  ###   ###  ###  ###              ROW  5 | . . . . .

    created by Paulina & Arek
    _______________________________________________________________________________________________________________________________________________
"""
+game_colours["TITEL_E"])

game_over = (game_colours["HELP_SCREEN_START"]+
"""
                    |GGGGGGG| |AAAAAAA| |M\      /M| |EEEEEE|      |OOOOO|  \VV\    /VV/ |EEEEEE| |RRRRRR|   
                    |GG|      |AA| |AA| |MM\    /MM| |EE|         |OO   OO|  \VV\  /VV/  |EE|     |RR   RR|  
                    |GG||GGG| |AAAAAAA| |MMM\  /MMM| |EEEE|       |OO   OO|   \VV\/VV/   |EEEE|   |RRRRRR|   
                    |GG| |GG| |AA| |AA| |MM M\/M MM| |EE|         |OO   OO|    \VVVV/    |EE|     |RR|\RR\   
                    |GGGGGGG| |AA| |AA| |MM  MM  MM| |EEEEEE|      |OOOOO|      \VV/     |EEEEEE| |RR|  \RR\  
"""
+game_colours["HELP_SCREEN_END"])