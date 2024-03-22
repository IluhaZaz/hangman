import classes
from classes.game_class import lump, Handler
from random import choice
from utils.man_pictures import man
from lexicon.lexicon_ru import LEXICON_RU


MAX_MISTAKES = 6

handler = Handler()
handler.fsm = lump


@handler.filter_update(states=["default", "not_in_game"], commands=["start"])
def start_game(game: classes.Game):
    print(LEXICON_RU["start_game"])
    with open ("utils\\ru_dict.txt", mode = "r", encoding = "utf-8") as f:      
        game.word = choice(f.readlines()).replace("\n", "")
    game.guessed_word = "_" * len(game.word)
    print(f"{LEXICON_RU['word']}: {game.guessed_word}")
    lump.start()
    return True


@handler.filter_update(states=["in_game"], commands=["end"])
def end_game(game: classes.Game):
    print(LEXICON_RU["end_game"])
    game.clear()
    lump.end()
    return True


@handler.filter_update(states=["in_game"])
def guess_letter(game: classes.Game):
    letter: str = handler.update
    if not (letter.isalpha() and len(letter) == 1):
        print(LEXICON_RU["correct_letter"])
        return True
    if letter in game.used_letters:
        print(LEXICON_RU["used_letter"])
    elif letter in game.word:
        game.used_letters.append(letter)
        game.guessed_word = game.open_letters(game.guessed_word, game.word, letter)
        if game.guessed_word == game.word:
            print(LEXICON_RU["win"])
            lump.end()
            game.clear()
            print(LEXICON_RU["wanna_play"])
            return True
    else:
        game.used_letters.append(letter)
        print(man[game.mistakes])
        game.mistakes += 1
        if game.mistakes >= MAX_MISTAKES:
            print(LEXICON_RU["defeat"])
            print(f"{LEXICON_RU['word_was']}: {game.word}")
            lump.end()
            game.clear()
            print(LEXICON_RU["wanna_play"])
            return True
        else:
            print(LEXICON_RU["no_letter"])
    print(f"{LEXICON_RU['word']}: {game.guessed_word}, {LEXICON_RU['used_letters']}: {game.used_letters}")
    return True


if __name__ == "__main__":

    game = classes.Game()

    print(LEXICON_RU["first_game"])

    while True:

        update = input()

        handler.update = update

        for func in [start_game, end_game, guess_letter]:
            if func(game):
                break