def show_balance():
    global balance
    print(f"Your balance is Ksh{balance:.2f}")

def deposit():
    global balance
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Please enter a positive amount.")
            return 0
        print(f"Ksh{amount:.2f} deposited successfully!" )
        return amount 
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return 0
    
def withdraw():
    global balance
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds. Withdrawal not processed.")
            return 0
        elif amount <= 0:
            print("Please enter a positive amount.")
            return 0 
        print(f"Ksh{amount:.2f} withdrawn successfully!")
        return amount
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return 0
    
def main():
    global balance
    balance = 0
    is_running = True

    while is_running:
        print("\nBanking Program")
        print("1.Show balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        choice = input("Enter your choice(1-4): ")

        if choice == '1':
            show_balance()
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw()
        elif choice == '4':
            is_running = False
            print("Thank you! Have a nice day!")
        else:
            print("Invalid choice! Please select a number between 1 and 4.")
   

if __name__ == "__main__":
    main()
