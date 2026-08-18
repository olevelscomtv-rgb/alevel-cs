class BankAccount:
    def __init__(self, accountNumber, ownerName, balance):
        self._accountNumber = accountNumber
        self._ownerName = ownerName
        self._balance  = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount

    def displayBalance(self):
        print (self._balance)


Account1 = BankAccount(3070, 'Taaha', 500)
Account1.deposit(100)
Account1.withdraw(150)
Account1.displayBalance()