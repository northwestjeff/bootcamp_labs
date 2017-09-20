

class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.int_rate = 0.001

    def get_funds(self):
        return "Total Available Balance: ${}".format(self.balance)

    def deposit(self, amount):
        self.balance += amount

    def check_withdrawl(self, amount):
        if int(self.balance) - int(amount) >= 0:
            # print("True: {} - {} is :".format(amount, self.balance), int(amount) - int(self.balance))
            return True
        else:
            # print("False: {} - {} is :".format(amount, self.balance), int(amount) - int(self.balance))
            return False

    def withdraw(self, amount):
        self.balance -= int(amount)


    def calc_interest(self):
        self.balance = self.balance * (1 + self.int_rate)


class Main:
    def __init__(self):
        self.checking = Account("checking")
        self.savings = Account("savings")
        self.accounts ={"1": self.checking, "2": self.savings}

    def account(self):
        account_select = input("Press 1 to view Checking, 2 to view Savings: ")
        # account_select = "1"
        return account_select

    def menu(self, account_select):
        running = True
        while running == True:
            self.user_input = input("Press 1 to view balance, 2 to deposit, 3 to withdraw, Any other key to quit. ")
            if self.user_input is "1":
                # View account balance
                print(self.accounts.get(account_select).get_funds())
            elif self.user_input is "2":
                # Deposit funds
                dep_amount = int(input("How much would you like to deposit?: "))
                self.accounts.get(account_select).deposit(dep_amount)
                print(self.accounts.get(account_select).get_funds())
            elif self.user_input is "3":
                # Withdraw Funds
                with_amount = int(input("How much would you like to withdraw?: "))
                if self.accounts.get(account_select).check_withdrawl(with_amount) == True:
                    self.accounts.get(account_select).withdraw(with_amount)
                    print(self.accounts.get(account_select).get_funds())
                else:
                    print("insufficient funds!  Please withdraw an amount less than or equal to your balance.")
                    print(self.accounts.get(account_select).get_funds())
            else:
                running = False

    def atm(self):
        atm = True
        while atm == True:
            account_type = game.account()
            game.menu(account_type)
            leave = input("press 1 to choose another account, any other key to quit. ")
            if leave != "1":
                atm = False

# game = Main()
# game.atm()
#
