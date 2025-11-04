class Customer:
    bankname="State Bank of India"
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
print("welcome to", Customer.bankname)
name=input("Enter Your Name:")
c=Customer(name)
while True:
    print("d-deposit \nw-withdraw \nc-check_balance \ne-exits")
    option=input("choose your option:")
    if option.lower()=="d":
        amount=float(input("enter amount to deposit:"))
        c.deposit(amount)
    elif option.lower()=="w":
        amount=float(input("enter amount to withdraw:"))
        c.withdraw(amount)
    elif option.lower()=="c":
        c.check_balance()
    elif option.lower()=="e":
        print("thanks for Banking...")
        break
    else:
        print("Invalid option please choose valid option")
