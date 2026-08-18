class BankAccount:
    def __init__(self, accountNumber, ownerName, balance):
        self.accountNumber = accountNumber
        self.ownerName = ownerName
        self.__balance  = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self.__balance -= amount

    def displayBalance(self):
        print (self.__balance)


Account1 = BankAccount(3070, 'Taaha', 500)
Account1.deposit(100)
Account1.withdraw(150)
Account1.displayBalance()