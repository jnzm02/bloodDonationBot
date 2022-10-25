def greeting_message() -> str:
    return "Blood donation is one of the noblest deeds that man can do. A donor gives some part of himself to save " \
           "a life. Therefore, it is important to be utterly ready for this journey. Let us help you to become a hero!"


def ask_for_ready() -> str:
    return "Now select an item from the menu to continue👇"


def question1() -> str:
    return "1) Вам есть 18 лет?"


def fail_question() -> str:
    return "We are sorry to inform you about your ineligibility for blood donation. However, those questions are " \
           "time-based; therefore, you can donate blood at the Astana blood center whenever the restricted time period" \
           " passes and you will be ready! If you have specific questions, choose the ASK A QUESTION item on menu."


def question2() -> str:
    return "2) Ваш вес больше 50?"


def fail_question2() -> str:
    return "Извините но мы не можем брать кровь у тех у кого вес меньше 50"


def success() -> str:
    return "Поздравляю!, вы нам подходите!🥳🥳🥳 \nСвяжитесь с членами Red Crescent Club по дальнейшим вопросам"


def send_status(user) -> str:
    return "Йо Аброр челик {} {} @{} готов к донорству".format(user.first_name, user.last_name, user.username)


def learn_more() -> str:
    return "Learn more on our instagram page: @nu_red_crescent"

def articles() -> str:
    return "More about blood donation:\n" \
           "1. Nutrition of the donor\n" \
           "2. Main benefits of blood donation\n" \
           "3. Breaking stereotypes: why you don’t donate blood\n" \
           "4. Who cannot donate blood? Contraindications\n" \
           "5. What will happen to the donor’s blood?\n" \
           "6. Frequently asked questions"
