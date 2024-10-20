class BankAccount:
    def __init__(self,account_number,date_of_opening,balance,customer_name):
        self.account_number=account_number
        self.date_of_opening=date_of_opening
        self.balance=balance
        self.customer_name=customer_name

        def deposit(self,amount):
            self.balance += amount
            return f"Amount deposited:{amount}"
        
        def withdraw(self,amount):
            if amount > self.balance:
                return "insufficient balance"
            else:
                self.balance -= amount
                return f"Amount withdrawn:{amount}"                
        def check_balance(self):
            print(f"cuurrent balance: {self.balance}.")

        def customer_details(self):
            print(f"customer_name:{self.customer_name}")
            print(f"Account_number:{self.account_number}")
            print(f"date_of_opening:{self.date_of_opening}")
            print(f"balance:{self.balance}\n")

account = BankAccount(account_number="20009", date_of_opening="20-06-2024", balance="1000", customer_name="Meggy Adeka")

print(account.deposit(600))
print(account.withdraw(150))
print(account.check_balance)
print ("customer details:")