# ATM Simulator

## Description

📝 Task — "Simple ATM / Cash Machine"
Create a program called atm.py that simulates a basic cash machine.

Starting balance: balance = 1000

The program should show a menu in a loop:

text
--- ATM MENU ---
1. Check balance
2. Deposit money
3. Withdraw money
4. Exit
Choose an option (1-4):
Rules for each option:

Check balance → print the current balance, e.g. "Your balance is: 1000".

Deposit → ask for an amount. If it's positive, add it to the balance and confirm. If not, show an error and don't change anything.

Withdraw → ask for an amount.

If the amount is greater than the balance → "Insufficient funds ❌"

If the amount is negative or zero → "Invalid amount ❌"

Otherwise → subtract it and confirm.

Exit → print "Goodbye! 👋" and stop the program (break).

If the user types an invalid menu option, show "Invalid option, try again." and keep looping.

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
