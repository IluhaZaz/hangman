"""from classes.game_class import Matter
from functools import wraps


def Filter(FSM: Matter, state: str, command: str):
    def real_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

    return real_decorator"""
