'''
Pedro Ramirez
Class: CS 521 - Spring 1
Date: 3/3/2023
Final Project
Description:
Parent class for the User class.
It will contain the bank information,
and universal attributes and method.
'''


class Bank:
    '''
    Parent class for the User class.
    contains private attributes for the bank information,
    '''

    __TITLE = 'The Boston Bank'
    __ADDRESS = '123 Main Street, Boston, MA 02134'

    def __init__(self, balance=0.0, account_number=0) -> None:
        self.balance = balance
        self.account_number = account_number

    def bank_info(self) -> str:
        '''
        customized string representation
        of the bank information.
        '''
        return f'---- {self.__TITLE} ----\n{self.__ADDRESS}\n'
