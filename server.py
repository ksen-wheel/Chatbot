__all__ = [
    'login',
]


from datetime import datetime
from model import *


# Создание тестовых данных
user1 = User('Иван', 'Иванов', 'Иванович', 'ivanov@yandex.ru', 'qwerty1')
user2 = User('Петр', 'Петровв', 'Петроович', 'petrov@yandex.ru', 'qwerty2')
user3 = User('Сидор', 'Сидоров', 'Сидорович', ' sidorov@yandex.ru', 'qwerty3')
account1_1 = user1.open_account()
account2_1 = user2.open_account()
account2_2 = user2.open_account()
account1_1.do_operation(datetime.fromisoformat('2022-05-01+10:02:00'), 1000, 'Зачисление зарплаты от ООО Рога и копыта')
account1_1.do_operation(datetime.fromisoformat('2022-05-02+14:34:12'), -200, 'Снятие наличных')
account1_1.do_operation(datetime.fromisoformat('2022-05-03+18:28:43'), -300, 'оплата мобильной связи')
account2_1.do_operation(datetime.fromisoformat('2022-05-04+08:52:41'), 2000, 'Зачисление зарплаты от Банка Ромашка')
account2_1.do_operation(datetime.fromisoformat('2022-05-05+12:09:00'), 3000, 'Зачиление зарплаты от Банка Ромашка')
account2_1.do_operation(datetime.fromisoformat('2022-05-06+19:42:00'), -800, 'Оплата коммунальных услуг')
account2_1.do_operation(datetime.fromisoformat('2022-05-07+15:42:00'), -700, 'Покупка в супермаркете')
account1_1.generate_statement(datetime.fromisoformat('2022-05-01'), datetime.fromisoformat('2022-05-04'))
account2_1.generate_statement(datetime.fromisoformat('2022-05-04'), datetime.fromisoformat('2022-05-07'))
account2_2.generate_statement(datetime.fromisoformat('2022-05-01'), datetime.fromisoformat('2022-05-10'))

users = {
    user1.email: user1, user2.email: user2, user3.email: user3
}


def login(email, password):
    if email not  in users:
        raise ValueError('Неизвестный пользователь')
    if password != users[email].password:
        raise ValueError('Некорректый пароль')
    return users[email]
