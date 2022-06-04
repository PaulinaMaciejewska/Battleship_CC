# colours #ship, target, separation, missed, empty)
import string
game_colours={
    "SS":'\033[1;34;40m',"SE":'\033[0;37;40m', #ship start
    "TS":'\033[1;31;40m',"TE":'\033[0;37;40m', #shot on target
    "BS":'\033[0;37;40m',"BE":'\033[0;37;40m', #separation buffor arroud the ship
    "MS":'\033[0;49;40m',"ME":'\033[0;37;40m', #missed shot
    "ES":'\033[0;49;36m',"EE":'\033[0;37;40m',#unused space - let as call it ocean
    "DS":'\033[7;49;91m',"DE":'\033[0;37;40m',#sunk ship
    "ERROR_STA":'\033[1;31;40m',"ERROR_END":'\033[0;37;40m',   #error messages
    "MESSE_STA":'\033[1;32;40m',"MESSE_END":'\033[0;37;40m',   #stetem resond messages
    "HELP_SCREEN_START":'\033[3;32;40m', "HELP_SCREEN_END":'\033[0;37;40m', #hepl messages
    "STATUS_BAR_AVAILLABLE_S":'\033[7;49;32m', "STATUS_BAR_AVAILLABLE_E":'\033[0;37;40m', #status bar  availlable 
    "STATUS_BAR_USED_S":'\033[7;49;91m',"STATUS_BAR_USED_E":'\033[0;37;40m', #status bar used
    "TITEL_S":'\033[0;37;40m',"TITEL_E":'\033[0;37;40m', #status bar used
    }

board_signes = {
    "ship":game_colours["SS"]+f"0"+game_colours["SE"],
    "separation":game_colours["BS"]+f"*"+game_colours["BE"],
    "empty":game_colours["ES"]+f"."+game_colours["EE"], 
    "missed":game_colours["MS"]+f'M'+game_colours["ME"],
    "hit":game_colours["TS"]+f'H'+game_colours["TE"],
    "sunk":game_colours["DS"]+f'S'+game_colours["DE"]
}

alphabet_max = string.ascii_uppercase
players_availlable = {1: ["Human","ANONYMUS"], 2: ["Computer", "BI"]}
ship_direction = ["H","V"]
board_size_sep = " "
board_maximal_rang = 26
game_command = ['play', 'quit', 'help','stat']
game_difficult = {1: ["Easy",200], 2: ["Mid",100], 3: ["HARD",70]}
game_who_play = {1:['Human', 'Human'],2:['Human','Computer'], 3:['Computer', 'Human'], 4:['Computer', 'Computer']}
