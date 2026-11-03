# ATM Simulator

## Description

Simple ATM simulation written in Python.

## Code

```python
balance = 1000

while True:
    print("\n--- ATM MENU ---")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")

    option = input("Choose an option (1-4): ")

    if option == "1":
        print(f"Your balance is: {balance}")

    elif option == "2":
        amount = float(input("How much do you want to deposit? "))

        if amount > 0:
            balance += amount
            print(f"Deposited {amount}. New balance: {balance}")
        else:
            print("Invalid amount ❌")

    elif option == "3":
        amount = float(input("How much do you want to withdraw? "))

        if amount <= 0:
            print("Invalid amount ❌")

        elif amount > balance:
            print("Insufficient funds ❌")

        else:
            balance -= amount
            print(f"Withdrew {amount}. New balance: {balance}")

    elif option == "4":
        print("Goodbye! 👋")
        break

    else:
        print("Invalid option, try again.")
```

## Concepts Practiced

- Variables
- Input / Output
- if / elif / else
- while loops
- break
- Arithmetic operators
- f-strings
