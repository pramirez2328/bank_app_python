import unittest
from user import User

user = User()
name = user.add_name()
last = user.add_last()
age = user.add_age()
amount = user.initial_amount()
email = user.add_email()
username = user.add_username()
password = user.add_password()


class TestFunctions(unittest.TestCase):
    def test_add_name(self):
        self.assertEqual(name, 'Pedro')
        assert isinstance(name, str)

    def test_add_last(self):
        self.assertEqual(last, 'Lara')
        assert isinstance(last, str)

    def test_add_age(self):
        self.assertEqual(age, 30)
        assert isinstance(age, str)

    def test_initial_amount(self):
        self.assertEqual(amount, 100.0)
        assert isinstance(amount, float)

    def test_add_email(self):
        self.assertEqual(email, 'prlara@yahoo.com')
        assert isinstance(email, str)

    def test_add_username(self):
        self.assertEqual(username, 'prlara')
        assert isinstance(username, str)

    def test_add_password(self):
        self.assertEqual(password, 'Ramirez123')
        assert isinstance(password, str)


if __name__ == '__main__':
    unittest.main()
