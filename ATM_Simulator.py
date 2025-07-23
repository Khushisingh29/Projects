#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3

conn = sqlite3.connect("ATM.db")
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS accounts(
    acc_no INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    pin TEXT,
    balance REAL
)
''')

conn.commit()
def create_account(name, pin, balance):
    cur.execute("INSERT INTO accounts(name, pin, balance) VALUES (?, ?, ?)", (name, pin, balance))
    conn.commit()
    print(" Account created successfully!")

create_account('Khushi', 1234, 5000)


# In[2]:


def login(acc_no, pin):
    cur.execute("SELECT * FROM accounts WHERE acc_no=? AND pin=?", (acc_no, pin))
    user = cur.fetchone()
    if user:
        print(f" Welcome {user[1]}!")
        return user
    else:
        print(" Invalid account number or PIN.")
        return None

def check_balance(acc_no):
    cur.execute("SELECT balance FROM accounts WHERE acc_no=?", (acc_no,))
    balance = cur.fetchone()[0]
    print(f"Current Balance: {balance}")
def deposit(acc_no, amount):
    cur.execute("UPDATE accounts SET balance = balance + ? WHERE acc_no=?", (amount, acc_no))
    conn.commit()
    print(f" {amount} deposited successfully.")
def withdraw(acc_no, amount):
    cur.execute("SELECT balance FROM accounts WHERE acc_no=?", (acc_no,))
    current_balance = cur.fetchone()[0]

    if amount > current_balance:
        print(" Insufficient balance!")
    else:
        cur.execute("UPDATE accounts SET balance = balance - ? WHERE acc_no=?", (amount, acc_no))
        conn.commit()
        print(f" {amount} withdrawn successfully.")


# In[3]:


def ATM_menu():
    print("===== Welcome to Python ATM =====")
    acc_no = int(input("Enter Account Number: "))
    pin = int(input("Enter PIN: "))

    user = login(acc_no, pin)
    if not user:
        return

    while True:
        print("\n--- Main Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            check_balance(acc_no)
        elif choice == '2':
            amt = float(input("Enter amount to deposit: "))
            deposit(acc_no, amt)
        elif choice == '3':
            amt = float(input("Enter amount to withdraw: "))
            withdraw(acc_no, amt)
        elif choice == '4':
            print(" Thank you for using the ATM. Bye!")
            break
        else:
            print("Invalid choice.")
ATM_menu()
conn.close()


# In[ ]:




