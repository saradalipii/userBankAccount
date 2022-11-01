class BankAccount:
    # don't forget to add some default values for these parameters!
    accounts=[]
    def __init__(self, int_rate, balance): 
        self.int_rate=int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance+= amount
        return self

    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else: 
            print("not enough funds. Your balance: ",self.balance)
        return self

    def display_account_info(self):
        print(" balance is", self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        else: 
            print('Your account balance is negative')
        return self

    @classmethod
    def print_accounts(cls):
        for i in cls.accounts:
            print(i.display_account_info())

