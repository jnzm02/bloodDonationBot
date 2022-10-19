def greeting_message() -> str:
    return "Привет Донор!"


def ask_for_ready() -> str:
    return "Давайте проверим вашу готовность на сдачу крови"


def question1() -> str:
    return "1) Вам есть 18 лет?"


def fail_question1() -> str:
    return "Приходите когда вам исполнится 18!"


def question2() -> str:
    return "2) Ваш вес больше 50?"


def fail_question2() -> str:
    return "Извините но мы не можем брать кровь у тех у кого вес меньше 50"


def success() -> str:
    return "Поздравляю, вы нам подходите!🥳🥳🥳 \nСвяжитесь с членами Red Crescent Club по дальнейшим вопросам"


def send_status(user) -> str:
    return "Йо Аброр челик {} {} @{} готов к донорству".format(user.first_name, user.last_name, user.username)
