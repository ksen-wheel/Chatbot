from datetime import datetime
from random import randrange


class Operation:
    def __init__(self, date, amount, counterparty):
        self.date = date
        # Положительная сумма - пополнение счета, отрициательная сумма - снятие со счета.
        self.amount = amount
        self.counterparty = counterparty

    def __str__(self):
        return f'Дата: {self.date} Сумма: {self.amount} Контрагент: {self.counterparty}'


class Account:
    def __init__(self, balance, id, user):
        self.operations = []
        self.balance = balance
        self.id = id
        self.user = user
        self.statements = []

    def do_operation(self, date, amount, counterparty) -> Operation:
        if amount < 0 and self.balance + amount < 0:
            raise ValueError('отрициательный баланс не допустим')
        if amount == 0:
            raise ValueError('Нулевые операции не допустимы')
        self.balance += amount
        self.operations.append(Operation(date, amount, counterparty))
        return self.operations[-1]

    def generate_statement(self, from_date, to_date, receiver_email=None):
        operations = []
        for operation in self.operations:
            if from_date <= operation.date <= to_date:
                operations.append(operation)
        email = receiver_email if receiver_email else self.user.email
        self.statements.append(Statement(datetime.now(), self, operations, self.user, email, from_date, to_date))
        return self.statements[-1]

    def print(self):
        print(f'Операции на счету {self.id}')
        for operation in self.operations:
            print(operation)

    def print_statements(self):
       for number, statement in enumerate(self.statements, start=1):
           print(number, statement.summary(), sep=': ')

    def get_statement(self, number):
        return self.statements[number - 1]


class User:
    def __init__(self, name, surname, middle_name, email, password):
        self.name = name
        self.surname = surname
        self.middle_name = middle_name
        self.email = email
        self.password = password
        self.accounts = []

    def open_account(self):
        self.accounts.append(Account(0, randrange(1000, 10000), self))
        return self.accounts[-1]

    def print_accounts(self):
        print(f'Текущие счета пользователя{self.email}')
        for account in self.accounts:
            print(account.id, account.balance, sep=': ')

    def get_account(self, id):
        for account in self.accounts:
            if account.id == id:
                return account
        raise ValueError('Неизвестный номер счета')


class Statement:
    def __init__(self, creation_date, account, operations, user, receiver_email, from_date, to_date):
        self.creation_date = creation_date
        self.account = account
        self.operations = operations
        self.user = user
        self.receiver_email = receiver_email
        self.from_date = from_date
        self.to_date = to_date

    def send(self):
        print('>>>>')
        print(f'Выписка для счета {self.account.id} для пользователя {self.account.user.surname} {self.account.user.name} {self.account.user.middle_name}')
        print(f'Создано {self.creation_date}')
        print(f'Получатель {self.receiver_email}')
        print('Операции:')
        for operation in self.operations:
            print(operation)
        print('<<<<')

    def summary(self):
        return f'{self.from_date}-{self.to_date} {self.receiver_email}'

def login(email, password):
    if email not  in users:
        raise ValueError('Неизвестный пользователь')
    if password != users[email].password:
        raise ValueError('Некорректый пароль')
    return users[email]


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

#Начало интерактивной сессии
email = input('Email:')
password = input('Пароль:')
current_user = login(email, password)
current_user.print_accounts()
account_id = int(input('номер счета'))
current_account = current_user.get_account(account_id)
current_account.print()
from_date = datetime.fromisoformat(input('Начало периода'))
to_date = datetime.fromisoformat(input('конец периода'))
receiver_email = input('Почта получателя')
generated_statement = current_account.generate_statement(from_date, to_date, receiver_email)
generated_statement.send()
current_account.print_statements()
statement_number = input('Номер выписки')
current_account.get_statement(int(statement_number)). send()




