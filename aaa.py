import pprint
from datetime import datetime
now = datetime.now()
date_string = now.strftime("%d/%m/%Y")
date_string_split = date_string.split("/")
month = date_string_split[1]
year = date_string_split[2]

available_log_types = ['deposit', 'withdrawal', 'transfer_to', 'transfer_in', 'conversion']
basic_log = available_log_types[0:2]  # - Basic logs are made of str & int
medium_log = available_log_types[2:4]  # - Medium logs are lists
advanced_log = available_log_types[-1]  # - Advanced logs are dictionaries


class Account:
    def __init__(self, account_id: int, credit_limit: int, is_foreign_currency: bool):
        self.account_id = account_id
        self.credit_limit = credit_limit
        self.is_foreign_currency = is_foreign_currency
        self.transaction_db = {}
        self.balance = [{"ILS": 0}, {"USD": 0}]

    def __str__(self):
        details = f'- ACCOUNT #{self.account_id} -\nCREDIT LIMIT: {self.credit_limit:,} ILS\n' \
                  f'BALANCES:\n{self.balance[0]["ILS"]:,} ILS'
        return details if not self.is_foreign_currency else details + '\n' + f"{self.balance[1]['USD']:,} USD"

    def __repr__(self):
        return f"<ACCOUNT: {self.account_id}>"

    # LOG ACCOUNT ACTIONS IN DATABASE
    def log_transaction(self, tr_type: str, currency: str, amount: int, account: int = 'SELF'):
        if date_string not in self.transaction_db.keys():
            self.transaction_db[date_string] = {}
        if tr_type not in self.transaction_db[date_string].keys():
            self.transaction_db[date_string][tr_type] = []
        self.transaction_db[date_string][tr_type].append([{currency: amount}, account])


    # SHOW ACCOUNT LOGS
    def show_log(self):
        pprint.pprint(self.transaction_db)





