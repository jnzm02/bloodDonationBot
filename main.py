import messages
import telebot
import keyboard
from decouple import config

API_KEY = config('API_KEY')
SUPER_ADMIN_ID = int(config('ABROR_ID'))

bot = telebot.TeleBot(API_KEY)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    data = call.data
    if data == 'Fail1':
        bot.send_message(call.from_user.id, messages.fail_question1())

    if data == 'go_question2':
        question2(call.from_user)

    if data == 'Fail2':
        bot.send_message(call.from_user.id, messages.fail_question2())

    if data == 'success':
        success(call.from_user)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, messages.greeting_message())
    bot.send_message(message.chat.id, messages.ask_for_ready())
    bot.send_message(message.chat.id, messages.question1(), reply_markup=keyboard.question1())


def question2(user):
    bot.send_message(user.id, messages.question2(), reply_markup=keyboard.question2())


# def question3(user_id):
#     bot.send_message(user_id, messages.question3(), reply_keyboard=keyboard.question3())


def success(user):
    bot.send_message(user.id, messages.success())
    bot.send_message(SUPER_ADMIN_ID, messages.send_status(user))


bot.polling()
