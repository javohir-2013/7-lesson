from aiogram.fsm.state import StatesGroup, State


class UserState(StatesGroup):
    name = State()
    age = State()
    email = State()