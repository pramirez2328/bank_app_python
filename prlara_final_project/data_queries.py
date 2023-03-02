import sqlite3

from user import User

# Connect to the database
conn = sqlite3.connect('bank.db')

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
def add_account(user):
    with conn:
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

        print(
            f"Added account:\
        {user['account']}, {user['name']}, {user['balance']}"
        )


# # Function to delete an account by id
# def delete_account(id):
#     conn.execute(f"DELETE FROM accounts WHERE id = {id}")
#     conn.commit()
#     print(f"Deleted account with id: {id}")


# # Function to update an account's information
# def update_account(id, account_number=None, account_name=None, balance=None):
#     set_statements = []
#     if account_number:
#         set_statements.append(f"account_number = '{account_number}'")
#     if account_name:
#         set_statements.append(f"account_name = '{account_name}'")
#     if balance is not None:
#         set_statements.append(f"balance = {balance}")
#     set_clause = ", ".join(set_statements)
#     conn.execute(f"UPDATE accounts SET {set_clause} WHERE id = {id}")
#     conn.commit()
#     print(f"Updated account with id: {id}")


# # Function to display all account
def find_account(username, password):
    c.execute(
        "SELECT * FROM accounts WHERE username = ? AND password = ?",
        (username, password),
    )

    return c.fetchall()


# Main program loop
while True:
    print("Select an option:")
    print("1. Sign up")
    print("2. Sign in")
    print("3. Quit")
    choice = input("> ")

    if choice == "1":
        new_user = User()
        new_user.create_account()
        user = new_user.save_account()
        add_account(user)

    elif choice == "2":
        while True:
            user_username = input("Enter your username: ")
            user_password = input("Enter your password: ")
            user = find_account(user_username, user_password)
            if len(user) == 0:
                print("Invalid username or password. Please try again.")
                continue
            else:
                print(f'Welcome back {user[0][1]}!')
                break

    elif choice == "3":
        break

    else:
        print("Invalid choice. Please enter a number from 1-3.")

conn.close()
