from telebot.types import (
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton
)


def start_keyboard():
    keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        KeyboardButton("Articles📖"),
        KeyboardButton("Ask a question❓"),
        KeyboardButton("Check your eligibility for blood donation✅")
    )
    return keyboard


def articles():
    keyboard = InlineKeyboardMarkup(row_width=3)
    keyboard.add(
        InlineKeyboardButton("1", callback_data='1'),
        InlineKeyboardButton("2", callback_data='1'),
        InlineKeyboardButton("3", callback_data='1'),
        InlineKeyboardButton("4", callback_data='1'),
        InlineKeyboardButton("5", callback_data='1'),
        InlineKeyboardButton("6", callback_data='1')
    )
    return keyboard


def question1():
    keyboard = InlineKeyboardMarkup(row_width=2)

    keyboard.add(
        InlineKeyboardButton("Yes", callback_data="go_question2"),
        InlineKeyboardButton("No", callback_data="Fail")
    )

    return keyboard


def question2():
    keyboard = InlineKeyboardMarkup(row_width=2)

    keyboard.add(
        InlineKeyboardButton("Yes", callback_data="go_question3"),
        InlineKeyboardButton("No", callback_data="Fail")
    )

    return keyboard


def question3():
    keyboard = InlineKeyboardMarkup(row_width=2)

    keyboard.add(
        InlineKeyboardButton("Yes", callback_data="go_question4"),
        InlineKeyboardButton("No", callback_data="Fail")
    )

    return keyboard


def question4():
    keyboard = InlineKeyboardMarkup(row_width=2)

    keyboard.add(
        InlineKeyboardButton("Yes", callback_data="go_question5"),
        InlineKeyboardButton("No", callback_data="Fail")
    )

    return keyboard


def question5():
    keyboard = InlineKeyboardMarkup(row_width=2)

    keyboard.add(
        InlineKeyboardButton("Yes", callback_data="go_question6"),
        InlineKeyboardButton("No", callback_data="Fail"),
        InlineKeyboardButton("Not applicable", callback_data="go_question6")
    )

    return keyboard


def question6():
    keyboard = InlineKeyboardMarkup(row_width=2)

    keyboard.add(
        InlineKeyboardButton("Yes", callback_data="go_question7"),
        InlineKeyboardButton("No", callback_data="Fail")
    )

    return keyboard


def question7():
    keyboard = InlineKeyboardMarkup(row_width=2)

    keyboard.add(
        InlineKeyboardButton("Yes", callback_data="go_question8"),
        InlineKeyboardButton("No", callback_data="Fail")
    )

    return keyboard


def question8():
    keyboard = InlineKeyboardMarkup(row_width=2)

    keyboard.add(
        InlineKeyboardButton("Yes", callback_data="go_question9"),
        InlineKeyboardButton("No", callback_data="Fail")
    )

    return keyboard


def question9():
    keyboard = InlineKeyboardMarkup(row_width=2)

    keyboard.add(
        InlineKeyboardButton("Yes", callback_data="go_question10"),
        InlineKeyboardButton("No", callback_data="Fail")
    )

    return keyboard


def question10():
    keyboard = InlineKeyboardMarkup(row_width=2)

    keyboard.add(
        InlineKeyboardButton("Yes", callback_data="go_question11"),
        InlineKeyboardButton("No", callback_data="Fail")
    )

    return keyboard


def question11():
    keyboard = InlineKeyboardMarkup(row_width=2)

    keyboard.add(
        InlineKeyboardButton("Yes", callback_data="success"),
        InlineKeyboardButton("No", callback_data="Fail")
    )

    return keyboard
