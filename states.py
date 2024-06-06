from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    bot_str = State()
    suphler = State()