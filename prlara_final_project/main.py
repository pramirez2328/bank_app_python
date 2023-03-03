import sqlite3
import os
from user import User

# Connect to the database
conn = sqlite3.connect(':memory:')

c = conn.cursor()

# Create a table for accounts
c.execute(
    '''
    CREATE TABLE IF NOT EXISTS accounts (
        account_number TEXT PRIMARY KEY NOT NULL,
        account_name TEXT NOT NULL,
        balance REAL NOT NULL,
        age INTEGER NOT NULL,
        email TEXT NOT NULL,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    );
    '''
)


# Function to add a new account
def add_account(user) -> bool:
    with conn:
        try:
            c.execute(
                "INSERT INTO accounts VALUES (?, ?, ?, ?, ?, ?, ?);",
                (
                    user['account'],
                    user['name'],
                    user['balance'],
                    user['age'],
                    user['email'],
                    user['username'],
                    user['password'],
                ),
            )
        except sqlite3.IntegrityError:
            print("Account already exists.")
            return False
        else:
            return True


def get_user(username, password) -> list:
    c.execute(
        "SELECT * FROM accounts WHERE username = ? AND password = ?",
        (username, password),
    )

    return c.fetchall()


def deposit(user):
    while True:
        try:
            amount = float(input("Enter the amount to deposit: "))
        except ValueError:
            print("Error", "Amount must be a number")
        else:
            break

    previous_balance = user[0][2]
    new_balance = previous_balance + amount
    c.execute(
        "UPDATE accounts SET balance = ? WHERE account_number = ?",
        (new_balance, user[0][0]),
    )
    conn.commit()
    print(f"Your previous balance was: {previous_balance}")
    print(f"Your new balance is: {new_balance}")


def withdraw(user):
    while True:
        try:
            amount = float(input("Enter the amount to withdraw: "))
        except ValueError:
            print("Error", "Amount must be a number")
        else:
            break

    previous_balance = user[0][2]
    new_balance = previous_balance - amount
    c.execute(
        "UPDATE accounts SET balance = ? WHERE account_number = ?",
        (new_balance, user[0][0]),
    )
    conn.commit()
    print(f"\n---- Your previous balance was: {previous_balance} ----")
    print(f"---- Your new balance is: {new_balance} ----")


def check_balance(user):
    print(f"\n---- Your balance is: {user[0][2]} ----\n")


def transactions_loop(username, password):
    while True:
        print("Select an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Logout")
        choice = input("> ")

        if choice == "1":
            user = get_user(username, password)
            deposit(user)

        elif choice == "2":
            user = get_user(username, password)
            withdraw(user)

        elif choice == "3":
            user = get_user(username, password)
            check_balance(user)

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please enter a number from 1-4.")


def greetings(new_user):
    print("\n* Account created successfully!")
    print(f"* Your new account number is: {user['account']}")
    print(new_user.bank_info())
    print(new_user)
    print('You can now make transactions!\n')


# Main program loop
if __name__ == "__main__":
    table_properties = [
        'account',
        'name',
        'balance',
        'age',
        'email',
        'username',
        'password',
    ]
    existing_users = {}
    path = os.path.join(os.path.dirname(__file__), '../existing_users.txt')
    db = open(path, 'r')
    for line in db:
        line = line.strip().split(',')
        index = 0
        for value in range(7):
            existing_users[table_properties[index]] = line[value]
            index += 1

        add_account(existing_users)

    while True:
        print('---- Welcome to the Boston bank! ----')
        print("Select an option:")
        print("1. Sign up")
        print("2. Sign in")
        print("3. Quit")
        choice = input("> ")

        if choice == "1":
            new_user = User()
            new_user.create_account()
            user = new_user.save_account()
            if add_account(user):
                greetings(new_user)
                transactions_loop(user['username'], user['password'])

        elif choice == "2":
            while True:
                user_username = input("Enter your username: ")
                user_password = input("Enter your password: ")
                current_user = get_user(user_username, user_password)
                if len(current_user) == 0:
                    print("Invalid username or password. Please try again.")
                    continue
                else:
                    print(f'\n---- Welcome back {current_user[0][1]}! ----\n')
                    transactions_loop(user_username, user_password)
                    break

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please enter a number from 1-3.")

    db.close()
conn.close()
