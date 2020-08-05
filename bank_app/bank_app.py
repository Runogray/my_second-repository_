import connect
class Bankaccount:
    def __init__(self):
        self.balance = 0
        print("welcome to simple bank app")
    
    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance += amount
        print("\nAmount deposited: ",amount)
    
    def withdraw(self):
        amount = float(input("Enter amount to deposit: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\nYou withdrew:", amount)
        else:
            print("Insufficient funds")
    
    def display(self):
        print("Net available balance =", self.balance)

slap = Bankaccount()
slap.deposit()
slap.withdraw()
slap.display()
