class BankAccount:
    def __init__(self, account_holder, user_id, balance=0.0):
        self.account_holder = account_holder
        self.user_id = user_id
        self.balance = balance

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} deposited successfully!")
        else:
            print("Invalid amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid amount. Please enter a positive value.")
        else:
            self.balance -= amount
            print(f"${amount:.2f} withdrawn successfully!")

def main():
    print("Welcome to the Bank!")
    
    # Ask for username and user ID
    username = input("Enter your username: ")
    user_id = input("Enter your user ID: ")

    # Create an account object
    account = BankAccount(account_holder=username, user_id=user_id)

    while True:
        print("\nBank Operations:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            account.check_balance()
        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == "4":
            print(f"Thank you, {account.account_holder} (User ID: {account.user_id}), for banking with us. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
