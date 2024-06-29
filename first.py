import json
import os
from datetime import datetime

TRANSACTIONS_FILE = "transactions.json"

transactions = []

if os.path.exists(TRANSACTIONS_FILE):
    with open(TRANSACTIONS_FILE, "r") as file:
        transactions = json.load(file)

def display_transactions():
    if not transactions:
        print("No transactions.")
    else:
        for i, transaction in enumerate(transactions, 1):
            print(f"{i}. {transaction['date']} - {transaction['category']}: ${transaction['amount']}")


def add_transaction():
    category = input("Enter transaction category (Income/Expense): ").capitalize()
    if category not in ['Income', 'Expense']:
        print("Invalid category. Please choose Income or Expense.")
        return
    
    amount = float(input("Enter the transaction amount: "))
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    transaction = {
        "date": date,
        "category": category,
        "amount": amount
    }
    transactions.append(transaction)
    save_transactions()
    print("Transaction added successfully!")

def calculate_budget():
    total_income = sum(transaction['amount'] for transaction in transactions if transaction['category'] == 'Income')
    total_expenses = sum(transaction['amount'] for transaction in transactions if transaction['category'] == 'Expense')
    remaining_budget = total_income - total_expenses
    return remaining_budget

def expense_analysis():
    expense_categories = {}
    for transaction in transactions:
        if transaction['category'] == 'Expense':
            category = transaction['category']
            amount = transaction['amount']
            if category not in expense_categories:
                expense_categories[category] = 0
            expense_categories[category] += amount

    if expense_categories:
        print("\nExpense Analysis:")
        for category, total in expense_categories.items():
            print(f"{category}: ${total}")


def save_transactions():
    with open(TRANSACTIONS_FILE, "w") as file:
        json.dump(transactions, file)

while True:
    print("\nBudget Tracker")
    print("1. Display Transactions")
    print("2. Add a Transaction")
    print("3. Calculate Budget")
    print("4. Expense Analysis")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        display_transactions()
    elif choice == "2":
        add_transaction()
    elif choice == "3":
        budget = calculate_budget()
        print(f"Remaining Budget: ${budget}")
    elif choice == "4":
        expense_analysis()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")

print("Goodbye!")