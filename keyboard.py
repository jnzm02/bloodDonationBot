from telebot.types import (
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton
)


def question1():
    keyboard = InlineKeyboardMarkup(row_width=2)

    keyboard.add(
        InlineKeyboardButton("Да", callback_data="go_question2"),
        InlineKeyboardButton("Нет", callback_data="Fail1")
    )

    return keyboard


def question2():
    keyboard = InlineKeyboardMarkup(row_width=2)

    keyboard.add(
        InlineKeyboardButton("Да", callback_data="success"),
        InlineKeyboardButton("Нет", callback_data="Fail2")
    )

    return keyboard
