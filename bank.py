class bank:
    # INIT CONSTRUCTOR
    def __init__(self, name, account_number, balance=0.00):
        """
        Initializes a bank account:

        This constructor sets up the account with the given name,
        account number, and an optional starting balance which defaults to 0.
        """
        self.name = name
        self.account_number = account_number
        self.balance = balance

    # DEPOSIT FUNCTION
    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            print("Deposit failed: amount must be a number.")
            return

        if amount > 0:
            self.balance = self.balance + amount
            print("Deposited $" + str(amount) + " to " + self.name + "'s account.")
        else:
            print("Deposit amount must be positive.")

        """
        Deposit money into the account.

        Adds the specified `amount` to the current balance if it's a positive number.
        Otherwise, prints an error message.
        """

    # WITHDRAW FUNCTION
    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            print("Withdrawal failed: amount must be a number.")
            return

        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance = self.balance - amount
            print("Withdrew $" + str(amount) + " from " + self.name + "'s account.")

        """
        Withdraw money from the account.

        Deducts the specified `amount` from the balance if it's a positive number
        and sufficient funds are available. Otherwise, prints an error message.
        """

    # PRINT BALANCE FUNCTION
    def print_balance(self):
        print(self.name + "'s Account Balance: $" + str(self.balance))

    """
        Print the current account balance.

        Displays the account holder's name along with the current balance.
        """


# TESTING-------------------

account = bank("Avyukt", "12345678", 100.00)
print("\nInitial Balance Check")
account.print_balance()
print("\nValid Deposit")
account.deposit(150.00)
print("\nInvalid Deposit (Zero)")
account.deposit(0.00)
print("\nInvalid Deposit (Negative)")
account.deposit(-50.00)
print("\nBalance After Deposits")
account.print_balance()
print("\nValid Withdrawal")
account.withdraw(100.00)
print("\nInvalid Withdrawal (Zero)")
account.withdraw(0.00)
print("\nInvalid Withdrawal (Negative)")
account.withdraw(-30.00)
print("\nInvalid Withdrawal (Insufficient Funds)")
account.withdraw(1000.00)
print("\nFinal Balance Check")
account.print_balance()

print("\n")

account2 = bank("John", "2345610")
print("\nInitial Balance Check")
account2.print_balance()
print("\nValid Deposit")
account2.deposit(50.00)
print("\nInvalid Deposit (Zero)")
account2.deposit(0.00)
print("\nInvalid Deposit (Negative)")
account2.deposit(-50.00)
print("\nBalance After Deposits")
account2.print_balance()
print("\nValid Withdrawal")
account2.withdraw(10.00)
print("\nInvalid Withdrawal (Zero)")
account2.withdraw(0.00)
print("\nInvalid Withdrawal (Negative)")
account2.withdraw(-30.00)
print("\nInvalid Withdrawal (Insufficient Funds)")
account2.withdraw(1000.00)
print("\nFinal Balance Check")
account2.print_balance()
