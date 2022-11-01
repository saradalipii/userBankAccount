from bankAccount import BankAccount
class User:

    def __init__(self,name):
        self.name=name
        self.account={  
            "checking": BankAccount(0.1,1000),
            "savings": BankAccount(0.5, 100)
        }

    def print_balance(self):
        print("Savings balance is ",self.account['savings'].balance ,"and Checking balance is ",self.account['checking'].balance)

    def transfert(self, user2, amount):
        self.account["checking"].withdraw(amount)
        user2.account["checking"].deposit(amount)
        return self


user1=User("1")
user2=User("2")
#user1.account["savings"].deposit(200).display_account_info()

user1.transfert(user2,200).print_balance() 
user2.print_balance()