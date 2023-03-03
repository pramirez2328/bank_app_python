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
    TITLE = 'The Boston Bank'
    ADDRESS = '123 Main Street, Boston, MA 02134'

    def __init__(self, balance=0.0, account_number=0) -> None:
        self.balance = balance
        self.account_number = account_number

    def bank_info(self) -> str:
        return f'---- {self.TITLE} ----\n{self.ADDRESS}\n'
