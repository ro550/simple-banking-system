import json
import os


class BankAccount:
    def __init__(self, username, filename="accounts.json"):
        self.username = username
        self.filename = filename
        self.balance = self.load_balance()

    def load_balance(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                return data.get(self.username, 0.0)
        return 0.0

    def save_balance(self):
        data = {}
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
        data[self.username] = self.balance
        with open(self.filename, "w") as f:
            json.dump(data, f)

    def show_balance(self):
        print(f"Your balance is Ksh{self.balance:.2f}")

    def deposit(self, amount):
        if amount <= 0:
            print("Please enter a positive amount.")
            return
        self.balance += amount
        self.save_balance()
        print(f"Ksh{amount:.2f} deposited successfully!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Please enter a positive amount.")
        elif amount > self.balance:
            print("Insufficient funds. Withdrawal not processed.")
        else:
            self.balance -= amount
            self.save_balance()
            print(f"Ksh{amount:.2f} withdrawn successfully!")


def main():
    print("Welcome to the CLI Banking System")
    username = input("Enter your account name: ").strip()
    account = BankAccount(username)

    while True:
        print("\n===== Banking Menu =====")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            account.show_balance()

        elif choice == '2':
            try:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif choice == '3':
            try:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif choice == '4':
            print("Thank you for using the banking system. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a number between 1 and 4.")


if __name__ == "__main__":
    main()
