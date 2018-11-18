#!/usr/bin/env python3

from bankreader.romania import RaiffeisenStatement
import os

statement_xls_path = os.path.join('test', 'statements', 'Extras_de_cont_12345678_20012018_31012018.xls')

statement = RaiffeisenStatement(xls_path=statement_xls_path)

print(statement.account_number)
print(statement.client.iban)
print(statement.client.client_address)

for transaction in statement.transactions:
    print(transaction.amount)
    print(transaction.description)
    print(transaction.is_income)
