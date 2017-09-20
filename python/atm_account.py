



class Account:
    def __init__(self, initial_balance, name):
        self.account_type = name
        self.balance = initial_balance
        self.int_rate = 0.001

    def get_funds(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def check_withdraw(self, amount):
        # if int(amount) > 1000:
        #     raise ValueError
        if int(self.balance) - int(amount) >= 0:
            # print("True: {} - {} is :".format(amount, self.balance), int(amount) - int(self.balance))
            return True
        else:
            # print("False: {} - {} is :".format(amount, self.balance), int(amount) - int(self.balance))
            return False


    def withdraw(self, amount):
        if int(self.balance) - int(amount) >= 0:
            self.balance -= int(amount)
            return self.balance
        else:
            raise ValueError

    def get_standing(self):
        if self.balance >= 1000:
            return True
