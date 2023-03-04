# bank_app_python

Bank program to emulate an actual ATM machine

- create by Pedro Ramirez
- March 3, 2023
- CS 521 - spring 1
- GitHub repository link https://github.com/pramirez2328/bank_app_python

ATM project contains:

1. main.py ................... main file, where the program initiates and custom methods store data

2. user.py.  ................. class to instance a new account, functions to validate input

3. bank.py  .................. parent class, containing general atributes and methods

4. existing_users.txt......... file with data to upload existing users to the database

5. test.py. .................. file to test all input functions

**Boston University**

The ATM program, which is a simple yet effective interface that mimics the functionalities of a real bank ATM. The program allows you to perform regular transactions such as checking your balance and adding or withdrawing money from your existing account.

To ensure a high level of security and privacy, the program requires you to provide personal information including your name, last name, age, email, initial balance, username, and password. Once you have successfully logged in, you will be able to add, withdraw, and check your balances.

The program has been designed with a logical file structure to ensure ease of use and reliability. The main.py file contains the logic to create and store new and existing accounts using sqlite3. The user.py file contains the User class which has been created to create and validate new accounts and utilizes the uuid module to generate unique account numbers. The bank.py file contains the User's parent class Bank, which includes general bank attributes and methods. Additionally, a text file containing existing users is fetched every time the program starts.

It is important to note that the program does not require any external libraries and can be easily installed and run on any computer with Python3 installed.

I hope that you find this program useful and user-friendly!

sincerely,

Pedro R.
