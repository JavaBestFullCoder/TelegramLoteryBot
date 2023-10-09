# States class
from aiogram.fsm.state import State, StatesGroup


class Stat(StatesGroup):
    # new State param
    numb = State()