# This code shows if each user had two bank accounts.
# Classes need to be capitalized
class Bank_Account:
    # whatever is put here is a global variable
    all_bank_accounts = []
    # classmethod is used when you are accessing something global (directly under class), whereas you can use regular def if it is not something global
    # the following __init__ are attributes specific to certain accounts.
    # when it says that the interest reate should be provided upon instantiation, it means that we should not have a default variable for it and it should be specified when creating an account.
    def __init__(self, int_rate, balance = 0): 
        # instance attributes go here
        self.int_rate = int_rate
        self.balance = balance
        Bank_Account.all_bank_accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    # display_account_info() and yield_interest were used when I was just doing bank account
    # def display_account_info(self):
    #     print(f"Balance: ${self.balance}")
    #     return self
    # def yield_interest(self):
    #     if self.balance > 0:
    #         self.balance = self.balance + (self.balance * self.int_rate)
    #         return self
    # commenting out the following class method because it is not too necessary to have in this scenario, but there is a working one on the other file with one account per user.
    # @classmethod
    # def all_bank_account_balances(cls):
    #     for each_account in cls.all_bank_accounts:
    #         print(f"Balance: ${each_account.balance}")
        # Chain methods of an instance (not a class), so nothing similar to return self is needed. In addition, the goal is just to print here.

# account1 and account2 do not have a user attached to the accounts, so they are not really doing anything too significant now that we have users liked to bank account in class User. Therefore, we can get rid of (I'll comment them out) the bank accounts created, the related chains, and Bank_Account.all_bank_account_balances() since we will not have accounts to put in the list.
# account1 = Bank_Account(0.045, 200)
# account2 = Bank_Account(0.04, 650)

# # for the methods where there is nothing in parentheses, we are only passing in the self value.
# account1.deposit(433).deposit(153).deposit(48).withdraw(198).yield_interest().display_account_info()
# account2.deposit(212).deposit(119).withdraw(13).withdraw(22).withdraw(29).withdraw(46).yield_interest().display_account_info()

# the following corresponds to the classmethod that is commented out.
# Bank_Account.all_bank_account_balances()


class User:
    all_users = [ ]
    def __init__(self, name, savings_balance, checking_balance):
        self.name = name
        # account balance already has a default value, so we do not have to include that as a parameter. If the default wasn't zero, we would have to include it as a parameter.
        # Creating a new instance of bank account, like account1 = Bank_Account(0.045, 200). Make a dictionary to store the info multiple bank accounts.
        self.account = {
            "savings":Bank_Account(0.012, balance=savings_balance),
            "checking":Bank_Account(0.012, balance=checking_balance)
        }
        User.all_users.append(self)
    
    # Bank_Account does not have name in the class attribute, so you would keep in user.
    def display_user_balance(self):
        for key,info in self.account.items():
            print(f"{self.name}'s {key} Account Balance: ${info.balance}")
        return self

    # The following is for more practice. These are the following lines that correspond to this method: all_users = [ ], User.all_users.append(self), User.all_user_balances()
    @classmethod
    def all_user_balances(cls):
        for each_user in cls.all_users:
            # .account is representing the whole dictionary
            for key in each_user.account:
                # each_user is representing an instance of user in our account dictionary and the key part is allowing us to access each key in the dictionary. The .balance part is allowing us to target that attribute of the bank account.
                print(f"Balance of {key}: ${each_user.account[key].balance}")

# line below: creating an instance of User called sarah.
sarah = User("Sarah Perez", 45, 50)
catherine = User("Catherine Smith", 90, 62)
sally = User("Sally Miller", 120, 129)

# Looking at the parameters in make_deposit and make_withdrawal, we are passing sarah (what sarah is equal to) in as an argument for self and passing the numeric value in parentheses as an argument for amount
# Another way to do this assignment is to keep the methods from the user assignment and just call the deposit and withdraw methods from Bank_Account, then call the methods from User down here.
sarah.account["savings"].deposit(325).deposit(642).deposit(122).withdraw(236)
sarah.account["checking"].deposit(460).deposit(502).deposit(642).withdraw(98)
sarah.display_user_balance()

catherine.account["savings"].deposit(27).deposit(42).withdraw(6).withdraw(17)
catherine.account["checking"].deposit(62).deposit(52).withdraw(8).withdraw(14)
catherine.display_user_balance()

sally.account["savings"].deposit(657).withdraw(97).withdraw(46).withdraw(22)
sally.account["checking"].deposit(895).withdraw(88).withdraw(56).withdraw(65)
sally.display_user_balance()

User.all_user_balances()
# inside of the user has a Bank_Account instance