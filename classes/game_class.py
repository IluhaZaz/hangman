from transitions import Machine

class Matter(object):
    pass

lump = Matter()

states=['not_in_game', 'in_game']

transitions = [
    { 'trigger': 'start', 'source': 'not_in_game', 'dest': 'in_game' },
    { 'trigger': 'end', 'source': 'in_game', 'dest': 'not_in_game' }
]

machine = Machine(lump, states=states, transitions=transitions, initial='not_in_game')

class Game:
    def __init__(self) -> None:
        self.mistakes = 0
        self.word = ""
        self.used_letters = []

    def clear(self):
        self.mistakes = 0
        self.word = ""

if __name__ == "__main__":
    print(lump.state)
    pass