

import re


def send_email(message, recipient, sender="university.help@gmail.com"):

    def is_valid_email(email):                                               # Проверка на наличие "@" и корректных окончаний в email
        return bool(re.match(r"^[^@]+@[^@]+\.(com|ru|net)$", email))

    if not is_valid_email(recipient) or not is_valid_email(sender):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return


    if sender == recipient:                              # Проверка, не отправляем ли письмо себе
        print("Нельзя отправить письмо самому себе!")
        return


    if sender == "university.help@gmail.com":                        # Если отправитель по умолчанию
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email("Hello!", "student@example.com")
send_email("Hello!", "student@example.com", "custom.sender@example.com")
send_email("Hello!", "invalidemail.com", "student@example.com")
send_email("Hello!", "student@example.com", "student@example.com")








