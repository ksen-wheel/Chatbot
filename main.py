from datetime import datetime
from server import login


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
current_account.get_statement(int(statement_number)).send()
