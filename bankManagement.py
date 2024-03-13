import random

class Bank:
    def __init__(self, name, address):
        self.name = name
        self.users = []
        self.total_balance = 0
        self.total_loan = 0
        self.bankrupt = False
        self.loan_system = True  


class User:
    account_number_counter = 1000

    def __init__(self, name, email, address, accounttype, password):
        self.name = name
        self.email = email
        self.address = address
        self.accounttype = accounttype
        self.password = password
        self.balance = 0
        self.account_no = random.randint(1000, 10000)
        self.transaction_history = []
        self.loan_amount = 0
        self.loan_times = 0  

    def password_check(self, password):
        return self.password == password

    def deposite(self, bank, amount):
        if bank.bankrupt == False:
            if amount > 0:
                self.bank = bank
                self.balance += amount
                self.bank.total_balance += amount
                history = f"Successfully deposited: ${amount}. New Balance: ${self.balance}"
                self.transaction_history.append(history)
                print(history)
            else:
                print(f"Invalid deposit amount. Please Try again!")
        else:
            print("The bank is bankrupt, you cann't deposit money")


    def withdraw(self,bank, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded. Insufficient funds.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")

    def check_balance(self):
        return self.balance

    def check_transaction_history(self):
        return self.transaction_history

    def take_loan(self, bank, amount):
        self.bank = bank
        if self.bank.bankrupt == False:
            if self.bank.loan_system == True:
                if self.loan_times <= 2:
                    self.balance += amount
                    self.bank.total_balance -= amount
                    self.bank.total_loan += amount
                    history = f"Loan issued successfully and ${amount} added"
                    self.transaction_history.append(history)
                    self.loan_times += 1
                    print(history)
                else:
                    print("Sorry! Available for 2 times.")
            else:
                print(f"Currently loan is off")
        else:
            print(f"Bank Fokir, No loan available.")

    def transfer(self, recipient, amount):
        if recipient in self.bank.users:
            if amount <= self.balance:
                self.balance -= amount
                recipient.balance += amount
                self.transaction_history.append(f"Transferred ${amount} to {recipient.name}")
            else:
                print("Insufficient funds for the transfer.")
        else:
            print("Account does not exist for the transfer.")



class Admin:
    def __init__(self, bank):
        self.bank = bank
        self.name = "admin"
        self.password = "admin"

    def create_user(self, name, email, address, account_type, password):
        return self.bank.create_user(name, email, address, account_type, password)

    def delete_user(self, email):
        for user in self.bank.users:
            if user.email == email:
                self.bank.users.remove(user)
                print(f"User {user.name} deleted successfully.")
                return
        print("User not found.")
    def see_all_users(self):
        if len(self.bank.users) > 0:
            print(f"Available users down below")
            for user in self.bank.users:
                print(
                    f"Name: {user.name}, Account No: {user.account_no}, Email: {user.email}, Address: {user.address}, Account Type: {user.accounttype}"
                )
                print()
        else:
            print(f"No user found.")

    def check_total_balance(self):
        return self.bank.total_balance

    def check_total_loan_amount(self):
        return self.bank.total_loan

    def enable_loan_feature(self):
        self.bank.loan_system = True

    def disable_loan_feature(self):
        self.bank.loan_system = False


# Example usage:
class Authentication:
    def __init__(self) -> None:
        self.logged_in = None

    def Registration(self, bank, user):
        self.bank = bank
        self.user = user
        for users in bank.users:
            if self.user.email == users.email:
                print(f"Already Registered!")
                return
        self.bank.users.append(self.user)
        print(f"{self.user.name} account create successfully!")

    def login(self, bank, email, password):
        self.bank = bank
        for j in self.bank.users:
            if j.email == email and j.password == password:
                self.logged_in = j
                print(f"{j.name} logged in!")
                return True
        print("Email or password no match ")

    def log_out(self):
        self.logged_in = None


z = Bank("x", "y")
admin = Admin(z)
register = Authentication()

while True:
    print(f"Welcome to the {z.name} bank")
    print("Choose Admin or User")
    print("1. Admin")
    print("2. User")
    print("3. Exit")
    option = input("Choose One:")

    if option == "1":
        print("Admin info")
        user_name = input("Enter username:")
        password = input("Enter password:")
        if user_name == admin.name and password == admin.password:
            print("Logged in Successfully")
            while True:
                print("1. Create account for user")
                print("2. Show all user accounts")
                print("3. Show total available balance")
                print("4. Show total loan amount")
                print("5. Delete user account")
                print("6. Turn on/off loan system")
                print("7. Turn on/off bankrupt system")
                print("8. Log Out")
                option = input("Choose One:")

                if option == "1":
                    name = input("Enter user name:")
                    email = input("Enter user email:")
                    address = input("Enter user address:")
                    account_type = input(
                        "Enter '1' for 'Savings' type or Enter '2' for 'Current' type account: "
                    )
                    password = input("Enter user password:")
                    if account_type == "1":
                        new_user = User(name, email, address,
                                        "Savings", password)
                    elif account_type == "2":
                        new_user = User(name, email, address,
                                        "Current", password)
                    else:
                        print("Invalid account type. Please Try again!")
                    register.Registration(z, new_user)
                elif option == "2":
                    admin.see_all_users()  
                elif option == "3":
                    print(f"Total available balance: ${admin.check_total_balance()}")
                elif option == "4":
                    print(f"Total loan amount: ${admin.check_total_loan_amount()}")
                elif option == "5":
                    email = input("Enter email:")
                    admin.delete_user(email)
                elif option == "6":
                    option = input(
                        "Enter '1' for 'turned on' or Enter '2' for 'turned off':"
                    )
                    if option == "1":
                        admin.enable_loan_feature()
                    elif option == "2":
                        admin.disable_loan_feature()
                    else:
                        print("Invalid input. Please enter '1' or '2'")
                elif option == "7":
                    option = input(
                        "Enter '1' for 'turned on' or Enter '2' for 'turned off':"
                    )
                    if option == "1":
                        z.bankrupt = True
                    elif option == "2":
                        z.bankrupt = False
                    else:
                        print("Invalid input. Please enter '1' or '2'")
                elif option == "8":
                    break
                else:
                    print("Invalid selection. Please try again!")
        else:
            print("Invalid name or password. Please Try again!")
    elif option == "2":
        if len(z.users) > 0:
            print("Login as User")
            user_email = input("Enter user email:")
            password = input("Enter password:")
            log_in = register.login(z, user_email, password)
            if log_in:
                while True:
                    print("1. Show Balance")
                    print("2. Deposit Money")
                    print("3. Withdraw Money")
                    print("4. Transfer Money")
                    print("5. Transaction History")
                    print("6. Take Loan")
                    print("7. Log Out")
                    option = input("Enter Option:")
                    user = register.logged_in

                    if option == "1":
                        print(f"Balance: ${user.check_balance()}")
                    elif option == "2":
                        amount = int(input("Enter amount:"))
                        user.deposite(z,amount)

                    elif option == "3":
                        amount = int(input("Enter amount:"))
                        user.withdraw(z,amount)
                    elif option == "4":
                        name = input("Enter name of receiver:")
                        amount = int(input("Enter amount:"))
                        user.transfer(z, amount)
                    elif option == "5":
                        print(f"Transaction History: {user.check_transaction_history()}")
                    elif option == "6":
                        amount = int(input("Enter loan amount:"))
                        user.take_loan(z, amount)
                    elif option == "7":
                        register.log_out()
                        break
                    else:
                        print("Invalid options. Please Try again!")
            else:
                print("No Login User. Please Try again!")
        else:
            print("There are no users. Please contact with admin")
    elif option == "3":
        break
    else:
        print("No option match. Please Try again!")
