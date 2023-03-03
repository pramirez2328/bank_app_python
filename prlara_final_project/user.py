'''
create a class called User with the following attributes:
_init_ method
add_name(),
add_age(),
add_email(),
add_username(),
add_password(),
user_login(),
__repr__()
user_info()

'''
from typing import Dict
from bank import Bank
import uuid


class User(Bank):
    __incremental_id = 0

    def __init__(self, name='', age='', email='', username='', password=''):
        super().__init__()
        self.holder_name = name
        self.age = age
        self.email = email
        self.username = username
        self.password = password
        User.__incremental_id += 1

    def create_account(self) -> None:
        name = self.add_name()
        last = self.add_last()
        self.balance = self.initial_amount()
        self.holder_name = self.__add__(name, last)
        self.age = self.add_age()
        self.email = self.add_email()
        self.username = self.add_username()
        self.password = self.add_password()
        self.account_number = uuid.uuid4().hex[:8] + str(User.__incremental_id)

    def save_account(self) -> Dict:
        return {
            'name': self.holder_name,
            'balance': self.balance,
            'account': self.account_number,
            'age': self.age,
            'email': self.email,
            'username': self.username,
            'password': self.password,
        }

    def add_name(self) -> str:
        while True:
            name = input('Enter your name: ')
            try:
                for char in name:
                    if not char.isalpha():
                        raise ValueError
            except ValueError:
                print('Error', 'Name must contain only letters')

            else:
                break
        return name

    def add_last(self) -> str:
        while True:
            last = input('Enter your last name: ')
            try:
                for char in last:
                    if not char.isalpha():
                        raise ValueError
            except ValueError:
                print('Error', 'Name must contain only letters')
            else:
                break
        return last

    def initial_amount(self) -> float:
        while True:
            amount = input('Enter initial amount: ')
            try:
                if not float(amount):
                    raise ValueError
                if float(amount) < 0:
                    raise TypeError
            except ValueError:
                print('Error', 'Amount must be a number')
            except TypeError:
                print('Error', 'Amount must be greater than 0')
            else:
                break
        return float(amount)

    def add_age(self) -> int:
        while True:
            age = input('Enter your age: ')
            try:
                if not int(age):
                    raise ValueError
                if int(age) < 18:
                    raise TypeError()
            except ValueError:
                print('Error', 'Age must be a number')
            except TypeError:
                print(
                    'Error',
                    'You must be at least 18 years old to open an account',
                )
            else:
                break
        return age

    def add_email(self) -> str:
        while True:
            email = input('Enter your email: ')
            try:
                if self.__validate_email(email) is False:
                    raise ValueError
            except ValueError:
                print('Error', 'Enter a valid email')
            else:
                break
        return email

    def add_username(self) -> str:
        while True:
            username = input('Enter your username: ')
            try:
                if len(username) < 6:
                    raise ValueError
            except ValueError:
                print('Error', 'Username must be at least 6 characters long')
            else:
                break
        return username

    def add_password(self) -> None:
        while True:
            password = input('Enter your password: ')
            try:
                if len(password) < 8:
                    raise ValueError
            except ValueError:
                print('Error', 'Password must be at least 8 characters long')
            else:
                break
        return password

    def __add__(self, name, last):
        return name + ' ' + last

    def __validate_email(self, email) -> bool:
        import re

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.match(regex, email):
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f'\
     Your account information:\n\
     Account number: {self.account_number}\n\
     Name: {self.holder_name}\n\
     Balance: {self.balance}\n\
     Age: {self.age}\n\
     Email: {self.email}\n\
     Username: {self.username}\n\
     Password: {self.password}\n'
