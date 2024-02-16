#from utils.funcs import Filter

import classes
from classes.game_class import lump


command: str = ""

#@Filter(lump, "not_in_game", command)
def start_game():
    print("dkwodwdk")
    game.clear()
    lump.start()


func_dict = {
    "start": start_game
}


if __name__ == "__main__":

    game = classes.Game()

    while True:

        command = input()

        func = func_dict.get(command, None)
        if func:
            func()
        else:
            print("Не знаю такой команды")