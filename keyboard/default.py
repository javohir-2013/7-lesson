from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    button = KeyboardButton(text="Sherik kerak")
    button2 = KeyboardButton(text="Hodim kerak")
    button3 = KeyboardButton(text="Ish joyi kerak")
    button4 = KeyboardButton(text="Ustoz kerak")
    button5 = KeyboardButton(text="Shogird kerak")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button3],
            [button2, button4],
            [button5]
        ],
        resize_keyboard=True
    )
    return rkm




