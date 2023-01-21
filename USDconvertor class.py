class USDConverter:
    def __init__(self):
        self.sell_USD_rate = {}
        self.purchase_USD_rate = {}

    def add_exchange_rate(self, currency, rate):
        def add(currency, rate):
            self.sell_USD_rate[currency] = round(rate, 3)
            self.purchase_USD_rate[currency] = round(1 / rate, 3)

        if currency not in self.sell_USD_rate:
            add(currency, rate)
            print(f'{currency} added. \n'
                  f'1 USD = {self.sell_USD_rate[currency]} {currency}')
        elif currency in self.sell_USD_rate:
            add(currency, rate)
            print(f'Currency already exists.\n'
                  f'Rate successfully updated to {self.sell_USD_rate[currency]}')

    def display_exchange_rate(self, currency):
        print(f'1 USD  = {self.sell_USD_rate[currency]} {currency}\n'
              f'1 {currency} = {self.purchase_USD_rate[currency]} USD')

    def del_exchange_rate(self, currency):
        del self.sell_USD_rate[currency]
        del self.purchase_USD_rate[currency]
        print(f'{currency} was successfully deleted from system.')

    def currency_calculator(self, amount: float, currency_from: str, currency_to: str):
        if currency_from == 'USD':
            ret_value = self.sell_USD_rate[currency_to] * amount
        else:
            ret_value = self.purchase_USD_rate[currency_from] * amount
        print(f'{amount} {currency_from} = {ret_value} {currency_to}')

    def __str__(self):
        list_of_currencies = list(self.sell_USD_rate.items())
        ret_val = f'The exchange rate for USD is currently:\n'
        for key, value in list_of_currencies:
            ret_val = f'1 USD = {value} {key}\n'
            f'1 {key} = {self.purchase_USD_rate[key]} USD'
            ret_val += ret_val
        return ret_val


converter = USDConverter()
converter.add_exchange_rate('NIS', 3.16)
converter.add_exchange_rate('JPY', 113.73)
converter.add_exchange_rate('EUR', 0.89)
converter.display_exchange_rate('JPY')
converter.currency_calculator(30000, 'JPY', 'USD')
converter.currency_calculator(134, 'USD', 'EUR')
converter.add_exchange_rate('EUR', 0.96)
converter.del_exchange_rate('JPY')
converter.currency_calculator(3000, 'EUR', 'USD')
print(converter)
