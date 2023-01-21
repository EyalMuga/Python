class RavKav:
    km_pricing = {
        'short': 5.5,
        'medium': 12,
        'long': 23
    }

    def __init__(self, name: str, id_number: int):
        self.__name = name
        self.__id_number = id_number
        self.__balance = 0

        # log_history will indicate from str of date to list of the rides
        #     log_history = {
        #     23.11.2022 : (short,medium),
        #     24.11.2022 : (long)
        #     }

        self.log_history = {}

    def get_balance(self):
        return self.__balance

    def get_holder_id(self):
        return self.__id_number

    def get_holder_name(self):
        return self.__name

    def top_up(self, amount: int):
        if amount > 0:
            self.__balance += amount
        else:
            print("money must be greater than 0")

    def ride(self, km, datetime):
        if km < 15:
            if self.__balance >= 5.5:
                self.log_history[datetime] = ['short']
                self.__balance -= 5.5
            else:
                return 'not enough money'

        elif 15 < km < 40:
            if self.__balance >= 12:
                self.log_history[datetime] = ['medium']
                self.__balance -= 12
            else:
                return 'not enough money'

        elif km > 40:
            if self.__balance >= 23:
                self.log_history[datetime] = ['long']
                self.__balance -= 23
            else:
                return 'not enough money'

    # ride - given amount of km and datetime, purchase the ride and log it. Make sure to indicate
    # # If there is not enough money for the ride

    def __str__(self):
        return f"ride history {self.log_history}"


# checking

user1 = RavKav('eyal', 314894973)
user1.top_up(100)
user1.ride(12, '12.12.12')
user1.ride(22, '13.12.12')
print(user1.log_history)
print(user1.get_balance())
user2 = RavKav('moshe', 314892)
user2.top_up(14)
user2.ride(39, '12.12.22')
print(user2.log_history)
