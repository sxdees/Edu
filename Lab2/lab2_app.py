class BankApp:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance

    def transfer(self, target_account, amount):
        if not isinstance(target_account, BankApp):
            raise ValueError("Target account must be an instance of BankAccount.")
        self.withdraw(amount)
        target_account.deposit(amount)
        return self.balance, target_account.balance

    def get_balance(self):
        return self.balance

account1 = BankApp("Petr Ivanov", 15000)
account2 = BankApp("Andrew Petrov", 8000)

print("Balance of Mr Ivanov's account:", account1.get_balance())
print("Balance of Mr Petrov's account:", account2.get_balance())

account1.deposit(2500)
print("Mr Ivanov's balance after deposit:", account1.get_balance())

account1.withdraw(4200)
print("Mr Ivanov's balance after withdrawal:", account1.get_balance())

account1.transfer(account2, 1500)
print("Mr Ivanov's balance after transfer:", account1.get_balance())
print("Mr Petrov's balance after receiving transfer:", account2.get_balance())
