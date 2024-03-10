
import random
class Bank:
    def __init__(self, name, address) -> None:
        self.name = name
        self.users = []
        self.total_balance = 0
        self.total_loan = 0
        self.bankrupt = False
        self.loansystem = True

    def user(self, name, email, address, accounttype,password):
        self.name = name
        self.email = email
        self.address = address
        self.accounttype = accounttype
        self.password = password
        self.balance = 0
        self.account_no = random.randint(1000, 10000)
        self.transaction_history = []
        self.loan = 0

    def password_check(self, password):
        if self.password == password:
            return True
        else:
            return False
    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")
        return f"Deposited ${amount}"

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded. Insufficient funds.")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew ${amount}")

    def check_balance(self):
        return self.balance

    def check_transaction_history(self):
        return self.transactions

    def take_loan(self, amount):
        if self.loan_amount == 0:
            self.loan_amount += amount
            self.transactions.append(f"Loan taken: ${amount}")
        else:
            print("You can only take a loan at most two times.")

    def transfer(self, recipient, amount):
        if recipient in bank.users:
            if amount <= self.balance:
                self.balance -= amount
                recipient.balance += amount
                self.transactions.append(f"Transferred ${amount} to {recipient.name}")
            else:
                print("Insufficient funds for the transfer.")
        else:
            print("Account does not exist for the transfer.")


class Admin:
    def __init__(self, bank) -> None:
        self.bank = bank
        self.name = "admin"
        self.password = 123

    def create_user(self, name, email, address, account_type):
        return self.bank.create_user(name, email, address, account_type)

    def delete_user(self, user):
        self.bank.delete_user(user)

    def see_all_users(self):
        return self.bank.get_all_users()

    def check_total_balance(self):
        return self.bank.get_total_balance()

    def check_total_loan_amount(self):
        return self.bank.get_total_loan_amount()

    def enable_loan_feature(self):
        self.bank.enable_loan_feature()

    def disable_loan_feature(self):
        self.bank.disable_loan_feature()


# Example usage:
bank = Bank('x','k')
admin = Admin(bank)

user1 = bank.create_user("John Doe", "john@example.com", "123 Main St", "Savings")
user2 = bank.create_user("Jane Smith", "jane@example.com", "456 Oak St", "Current")

user1.deposit(1000)
user1.withdraw(500)
user1.take_loan(200)

user2.deposit(1500)

admin.create_user("Admin User", "admin@example.com", "789 Admin St", "Savings")

print("User 1 Balance:", user1.check_balance())
print("User 1 Transactions:", user1.check_transaction_history())
print("User 2 Balance:", user2.check_balance())
print("All Users:", admin.see_all_users())
print("Total Balance:", admin.check_total_balance())
print("Total Loan Amount:", admin.check_total_loan_amount())
