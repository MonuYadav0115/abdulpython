class Customer:
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("balance after deposit",self.balance)
    def check_balance(self):
        print("Your balance amonut is:",self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficint funds")
        else:
            self.balance=self.balance-amount
            print("balance after withdraw:",self.balance)


simha=Customer("monu")
simha.deposit(10000)
simha.withdraw(2000)
simha.withdraw(8000)
# simha.deposit(20000)
