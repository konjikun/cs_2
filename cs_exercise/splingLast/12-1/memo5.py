class Bank:
    def __init__(self, amounts):
        self._amounts = amounts.copy()

    def transfer(self, sender, receiver, yen):
        self._amounts[sender] -= yen
        self._amounts[receiver] += yen

bank = Bank({
    'alice': 1000000,
    'bob': 1234,
    'shop': 100000
})

bank.transfer('alice', 'bob', 300)
bank.transfer('bob', 'shop', 10000)
print(bank._amounts['alice'])