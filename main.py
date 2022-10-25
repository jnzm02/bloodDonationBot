import messages
import telebot
import keyboard
import time
from decouple import config

API_KEY = config('API_KEY')
SUPER_ADMIN_ID = int(config('ABROR_ID'))
GROUP_ID = int(config('GROUP_ID'))
RANDOM_GROUP_ID = int(config('RANDOM_GROUP_ID'))

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['check_bot'])
def check_bot_command(message):
    bot.send_message(RANDOM_GROUP_ID, "Hello, World!")


@bot.message_handler(commands=['q'])
def send_question_command(message):
    message_text = "User @" + str(message.from_user.username) + " asked question:\n"
    for text in message.text.split()[1:]:
        message_text += text + " "
    bot.send_message(RANDOM_GROUP_ID, message_text)
    bot.send_message(message.chat.id, "We'll contact you soon.")


@bot.message_handler(commands=['group_id'])
def get_group_id(message):
    print(message.chat.id)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, messages.greeting_message())
    bot.send_message(message.chat.id, messages.ask_for_ready(), reply_markup=keyboard.start_keyboard())


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    data = call.data
    last_message_id = call.message.message_id
    if data == 'Fail':
        bot.edit_message_reply_markup(call.from_user.id, message_id=last_message_id, reply_markup=None)
        time.sleep(0.5)
        bot.send_message(call.from_user.id, messages.fail_question())

    if data == '1':
        # bot.edit_message_reply_markup(call.from_user.id, message_id=last_message_id, reply_markup=None)
        # time.sleep(0.5)
        bot.send_message(call.from_user.id, messages.learn_more())

    if data == 'go_question2':
        bot.edit_message_reply_markup(call.from_user.id, message_id=last_message_id, reply_markup=None)
        time.sleep(0.5)
        bot.send_message(call.from_user.id, "Is your weight 50 kg and higher?", reply_markup=keyboard.question2())

    if data == 'go_question3':
        bot.edit_message_reply_markup(call.from_user.id, message_id=last_message_id, reply_markup=None)
        time.sleep(0.5)
        bot.send_message(call.from_user.id, "I have not consumed alcohol in 48 hours", reply_markup=keyboard.question3())

    if data == 'go_question4':
        bot.edit_message_reply_markup(call.from_user.id, message_id=last_message_id, reply_markup=None)
        time.sleep(0.5)
        bot.send_message(call.from_user.id, "I have not smoked for 2 hours", reply_markup=keyboard.question4())

    if data == 'go_question5':
        bot.edit_message_reply_markup(call.from_user.id, message_id=last_message_id, reply_markup=None)
        time.sleep(0.5)
        bot.send_message(call.from_user.id, "It’s been 5 days since my period (for girls)", reply_markup=keyboard.question5())

    if data == 'go_question6':
        bot.edit_message_reply_markup(call.from_user.id, message_id=last_message_id, reply_markup=None)
        time.sleep(0.5)
        bot.send_message(call.from_user.id, "I haven’t been vaccinated for 2 weeks", reply_markup=keyboard.question6())

    if data == 'go_question7':
        bot.edit_message_reply_markup(call.from_user.id, message_id=last_message_id, reply_markup=None)
        time.sleep(0.5)
        bot.send_message(call.from_user.id, "I haven’t had a tattoo/piercing in 6 months", reply_markup=keyboard.question7())

    if data == 'go_question8':
        bot.edit_message_reply_markup(call.from_user.id, message_id=last_message_id, reply_markup=None)
        time.sleep(0.5)
        bot.send_message(call.from_user.id, "I haven’t had a tooth removed in the last 10 days", reply_markup=keyboard.question8())

    if data == 'go_question9':
        bot.edit_message_reply_markup(call.from_user.id, message_id=last_message_id, reply_markup=None)
        time.sleep(0.5)
        bot.send_message(call.from_user.id, "It was one month since the recovery of my flu/sore throat", reply_markup=keyboard.question9())

    if data == 'go_question10':
        bot.edit_message_reply_markup(call.from_user.id, message_id=last_message_id, reply_markup=None)
        time.sleep(0.5)
        bot.send_message(call.from_user.id, "I haven’t been allergic for 2 months", reply_markup=keyboard.question10())

    if data == 'go_question11':
        bot.edit_message_reply_markup(call.from_user.id, message_id=last_message_id, reply_markup=None)
        time.sleep(0.5)
        bot.send_message(call.from_user.id, "I didn’t consume eggs, dairy products, smoked, spicy and fatty products the day before donation", reply_markup=keyboard.question11())

    if data == 'success':
        bot.edit_message_reply_markup(call.from_user.id, message_id=last_message_id, reply_markup=None)
        time.sleep(0.5)
        bot.send_message(call.from_user.id, "Congratulations! 🎉🎉🎉 You are eligible to donate blood based on common"
                                            " requirements! Now check our check-list to see permanent contraindications"
                                            " and make sure you are utterly ready to become a hero! Other than that "
                                            "welcome to our family of blood donors! If you have specific questions, "
                                            "choose the ASK QUESTION item on menu.")


@bot.message_handler(func=lambda message: True)
def message_handler(message):
    if message.text == "Check your eligibility for blood donation✅":
        bot.send_message(message.chat.id, "Are you 18 years old or above?", reply_markup=keyboard.question1())

    if message.text == 'Articles📖':
        bot.send_message(message.chat.id, messages.articles(), reply_markup=keyboard.articles())

    if message.text == 'Ask a question❓':
        bot.send_message(message.chat.id, "Please, start your question with command /q")
        bot.send_message(message.chat.id, "for example: '/q How can I contact member of Red Crescent Club?'")


bot.polling()
