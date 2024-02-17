from transitions import Machine
from functools import wraps


class Matter(object):
    pass

lump = Matter()

states=['default', 'not_in_game', 'in_game']

transitions = [
    { 'trigger': 'start', 'source': 'default', 'dest': 'in_game' },
    { 'trigger': 'start', 'source': 'not_in_game', 'dest': 'in_game' },
    { 'trigger': 'end', 'source': 'in_game', 'dest': 'not_in_game' }
]

machine = Machine(lump, states=states, transitions=transitions, initial='default')

class Handler:

    def __init__(self) -> None:
        self.fsm: Matter = None
        self.update: str = None
        self.handlers = []
        self.decorators = []
        self.funcs = []


    def filter_update(self, states: list[str] = [], commands: list[str] = []):
        def real_decorator(func):
            self.decorators.append(real_decorator)
            self.funcs.append(func)
            @wraps(func)
            def wrapper(*args, **kwargs):
                if (self.fsm.state in states or not states) and (self.update  in commands or not commands):
                    return func(*args, **kwargs)
                return None
            return wrapper
        return real_decorator     

class Game:
    def __init__(self) -> None:
        self.mistakes = 0
        self.word = ""
        self.guessed_word = ""
        self.used_letters = []

    def clear(self):
        self.mistakes = 0
        self.word = ""
        self.guessed_word = ""
        self.used_letters = []

    @staticmethod
    def open_letters(hidden: str, word: str, letter: str) -> str:
        new_hidden: str = ""
        for i in range(len(word)):
            if word[i] == letter:
                new_hidden += word[i]
            else:
                new_hidden += hidden[i]
        return new_hidden


if __name__ == "__main__":
    print(lump.state)
    pass