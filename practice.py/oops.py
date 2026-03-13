class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance
    
acc1 = BankAccount("Yash", 25000)
# acc1.deposit(5000)
acc1.withdraw(500)
print(acc1.get_balance())