from aiogram.dispatcher.filters.state import StatesGroup, State


class Reklama(StatesGroup):
    reklama = State()

class Call(StatesGroup):
    upload = State()
    download = State()

class Cart(StatesGroup):
    add = State()
    confirm = State()

class Stol(StatesGroup):
    start = State()
    down = State()


class Peredacha(StatesGroup):
    per = State()

class Prosto(StatesGroup):
    one = State()
    two = State()
    three = State()


class Card_Bar(StatesGroup):
    add = State()
