import classes
from classes.game_class import lump, Handler
from random import choice


MAX_MISTAKES = 5

handler = Handler()
handler.fsm = lump


@handler.filter_update(states=["default", "not_in_game"], commands=["start"])
def start_game(game: classes.Game):
    print("Игра началась")
    with open ("utils\\ru_dict.txt", mode = "r", encoding = "utf-8") as f:      
        game.word = choice(f.readlines())
    game.guessed_word = "_" * len(game.word)
    print(f"Ваше слово: {game.guessed_word}")
    lump.start()


@handler.filter_update(states=["in_game"], commands=["end"])
def end_game(game: classes.Game):
    print("Конец игры")
    game.clear()
    lump.end()


@handler.filter_update(states=["in_game"])
def guess_letter(game: classes.Game, letter: str):
    if letter in game.used_letters:
        print("Вы уже использовали эту букву")
    elif letter in game.word:
        game.used_letters.append(letter)
        game.guessed_word = game.open_letters(game.guessed_word, game.word, letter)
        if game.guessed_word == game.word:
            print("Победа")
            lump.end()
            game.clear()
            print("Хотите сыграть еще?")
    else:
        game.used_letters.append(letter)
        game.mistakes += 1
        if game.mistakes >= MAX_MISTAKES:
            print("Вы проиграли")
            lump.end()
            game.clear()
            print("Хотите сыграть еще?")
        else:
            print("Нет такой буквы")
    print(f"Ваше слово: {game.guessed_word}, использованные буквы: {game.used_letters}")


if __name__ == "__main__":

    game = classes.Game()

    while True:

        update = input()

        handler.command = update

        start_game(game)

        end_game(game)

        guess_letter(game, update)