__all__ = [
    'Operation',
    'Account',
    'User',
    'Statement',
]


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
