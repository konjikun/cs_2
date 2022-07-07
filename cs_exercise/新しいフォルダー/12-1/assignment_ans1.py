class Bank:
    def withdraw(self, name, yen):
        balance = self._amounts[name] - yen
        if balance >= 0:
            return balance
        else :
            None

bank = Bank({'bob': 1234})
balance = bank.withdraw('bob',234)
print(balance)
balance = bank.withdraw('bob',9999)
print(balance)