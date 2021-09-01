class BankAccount:

    all_accounts = []

    def __init__(self, acct, balance = 0, int_rate = 0.0025):
        self.balance = balance
        self.acct = acct
        self.int_rate = int_rate
        BankAccount.all_accounts.append(self)

    def deposit(self, amount, acct):
        self.balance += amount
        self.acct = acct
        return self
        
    def withdraw(self, amount, acct):
        self.balance -= amount
        self.acct = acct
        return self

    def display_account_info(self):
        print(f"Bank Account: {self.acct}, Account Balance: ${self.balance}")
        return self

    def yield_interest(self):
        self.balance = self.balance + (self.int_rate * self.balance)
        return self

    @classmethod
    def all_balances(cls):
        for account in cls.all_accounts:
            account.display_account_info()   

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount()
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account.balance}")

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self

bankUser1 = User("John Elway", "JohnE@denverbroncos.com")
bankUser2 = User("Peyton Manning", "PeytonM@denverbroncos.com")
bankUser3 = User("Karl Meklenburg", "KarlM@denverbroncos.com")