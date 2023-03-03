'''
Pedro Ramirez
Class: CS 521 - Spring 1
Date: 3/3/2023
Final Project
Description:
Test file for the bank application.
It will test the User class methods.
Test cases are written using the unittest module.
'''

import unittest
from user import User

# Create an instance of the User class
user = User()

# call the methods to fetch the user information
name = user.add_name()
last = user.add_last()
age = user.add_age()
amount = user.initial_amount()
email = user.add_email()
username = user.add_username()
password = user.add_password()


class TestFunctions(unittest.TestCase):
    '''Test the methods of the User class.'''

    def test_add_name(self):
        '''
        Check if the name is a string
        and if it is equal to Pedro.
        '''
        self.assertEqual(name, 'Pedro')
        assert isinstance(name, str)

    def test_add_last(self):
        '''
        Check if the last name is a string
        and if it is equal to Lara.
        '''
        self.assertEqual(last, 'Lara')
        assert isinstance(last, str)

    def test_add_age(self):
        '''
        Check if the age is an integer
        and if it is equal to 30.
        '''
        self.assertEqual(age, 30)
        assert isinstance(age, int)

    def test_initial_amount(self):
        '''
        Check if the initial amount is a float
        and if it is equal to 100.0
        '''
        self.assertEqual(amount, 100.0)
        assert isinstance(amount, float)

    def test_add_email(self):
        '''
        Check if the email is a string
        and if it is equal to prlara@yahoo.com
        '''
        self.assertEqual(email, 'prlara@yahoo.com')
        assert isinstance(email, str)

    def test_add_username(self):
        '''
        Check if the username is a string
        and if it is equal to prlara.
        '''
        self.assertEqual(username, 'prlara')
        assert isinstance(username, str)

    def test_add_password(self):
        '''
        Check if the password is a string
        and if it is equal to Ramirez123.
        '''
        self.assertEqual(password, 'Ramirez123')
        assert isinstance(password, str)


if __name__ == '__main__':
    unittest.main()
