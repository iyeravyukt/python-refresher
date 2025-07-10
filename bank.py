class bank:
    def __init__(self, name, account_number, balance = 0.00):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f"Deposited $" + amount + " to " + self.name + "'s account.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} from {self.name}'s account.")

    def print_balance(self):
        print(f"{self.name}'s Account Balance: ${self.balance:.2f}")

account = bank("Avyukt", "12345678", 100.00)

account.print_balance()
account.deposit(150.00)
account.withdraw(100.00)
account.print_balance()
account.withdraw(600.00) 
