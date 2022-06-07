class bank_account:
    # whatever is put here is a global variable
    all_bank_accounts = []
    # classmethod is used when you are accessing something global (directly under class), whereas you can use regular def if it is not something global
    # the following __init__ are attributes specific to certain accounts.
    # when it says that the interest reate should be provided upon instantiation, it means that we should not have a default variable for it and it should be specified when creating an account.
    def __init__(self, int_rate, balance = 0): 
        # instance attributes go here
        self.int_rate = int_rate
        self.balance = balance
        bank_account.all_bank_accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
            return self
    @classmethod
    def all_bank_account_balances(cls):
        for each_account in cls.all_bank_accounts:
            each_balance = each_account.balance
            print(f"Balance: ${each_balance}")
        # Chain methods of an instance (not a class), so nothing similar to return self is needed. In addition, the goal is just to print here.

# account1 and account2 do not have a user attached to the accounts, so they are not really doing anything too significant now that we have users liked to bank account in class User. Therefore, we can get rid of (I'll comment them out) the bank accounts created, the related chains, and bank_account.all_bank_account_balances() since we will not have accounts to put in the list.
# account1 = bank_account(0.045, 200)
# account2 = bank_account(0.04, 650)

# # for the methods where there is nothing in parentheses, we are only passing in the self value.
# account1.deposit(433).deposit(153).deposit(48).withdraw(198).yield_interest().display_account_info()
# account2.deposit(212).deposit(119).withdraw(13).withdraw(22).withdraw(29).withdraw(46).yield_interest().display_account_info()

# bank_account.all_bank_account_balances()


class User:
    all_users = [ ]
    def __init__(self, name):
        self.name = name
        # account balance already has a default value, so we do not have to include that as a parameter. If the default wasn't zero, we would have to include it as a parameter.
        # Creating a new instance of bank account, like on lines 32 and 33
        self.account = bank_account(0.012, 0)
        User.all_users.append(self)
    
    # bank_account does not have name in the class attribute, so you would keep in user.
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account.balance}")
        return self

    # The following is for more practice. These are the following lines that correspond to this method: all_users = [ ], User.all_users.append(self), User.all_user_balances()
    @classmethod
    def all_user_balances(cls):
        for each_user in cls.all_users:
            print(f"Balance: ${each_user.account.balance}")

# line below: creating an instance of User called sarah.
sarah = User("Sarah Perez")
catherine = User("Catherine Smith")
sally = User("Sally Miller")

# Looking at the parameters in make_deposit and make_withdrawal, we are passing sarah (what sarah is equal to) in as an argument for self and passing the numeric value in parentheses as an argument for amount
sarah.account.deposit(325).deposit(642).deposit(122).withdraw(236)
sarah.display_user_balance()

catherine.account.deposit(27).deposit(42).withdraw(6).withdraw(17)
catherine.display_user_balance()

sally.account.deposit(657).withdraw(97).withdraw(46).withdraw(22)
sally.display_user_balance()


User.all_user_balances()
# inside of the user has a bank_account instance