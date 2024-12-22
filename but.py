from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

MENU = ["камень", "ножницы", "бумага"]

keydord_main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="выбрать вариант")],
    ],
    resize_keyboard=True
)

def genrate_menu():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=menu)] for menu in MENU ],
        resize_keyboard=True
    )