'''
Bank class with the following attributes:
_init_ method
balance,
account_number,
holder_name,
deposit(),
withdraw(),
check_balance(),
__repr__()
'''


class Bank:
    accounts = list()

    def __init__(self, balance=0, account_number=0) -> None:
        self.balance = balance
        self.account_number = account_number

    def deposit(self, amount) -> None:
        self.balance += amount

    def withdraw(self, amount) -> None:
        self.balance -= amount

    def check_balance(self) -> int:
        return self.balance

    def __repr__(self) -> str:
        return "Acount number: {},\nHolder name: {},\nBalance: {}".format(
            self.account_number, self.holder_name, self.balance
        )
