class BankAcc:
    def __init__(self):
        self.__balance = 10000
        
    def chackBalance(self):
        print("Available Balance:- ", self.__balance)
    
    def deposit(self):
        amount = int(input("Enter Amount:- "))
        if amount > 0:
            self.__balance += amount
            print("Amount Deposited:- ", amount)
        else:
            print("Invalid Query")

    def withdraw(self):
        amount = int(input("Enter Amount:- "))
        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount Withdrawn:- ", amount)
            
        else:
            print("Invalid Query")

    # INR = Interest Rate calculation
    def INR(self):
        self.__inr = (self.__balance * 0.05)
        print("Interest Rate:- 5%")
        print("Your INR:- ", self.__inr)

b1 = BankAcc()

def saving():
    while True:
        print("--------------------------")
        print("To Chack Balance - 1")
        print("To Deposite - 2")
        print("To Withdraw - 3")
        print("To Chack INR - 4")
        print("To Exit - 5")
        
        op = int(input("Enter Query (1 to 5):- "))
        if op == 1:
            b1.chackBalance()
        elif op == 2:
            b1.deposit()
        elif op == 3:
            b1.withdraw()
        elif op == 4:
            b1.INR()
        elif op == 5:
            break
        else:
            print("Invalid Query")

def current():
    while True:
        print("--------------------------")
        print("To Chack Balance - 1")
        print("To Deposite - 2")
        print("To Withdraw - 3")
        print("To Chack INR - 4")
        print("To Exit - 5")
        op = int(input("Enter Query (1 to 5):- "))
        if op == 1:
            b1.chackBalance()
        elif op == 2:
            b1.deposit()
        elif op == 3:
            b1.withdraw()
        elif op == 4:
            print("No INR for this ACC type")
        elif op == 5:
            break
        else:
            print("Invalid Query")
            
AccType = input("Enter Acc Type:- ").lower()

if AccType == "saving":
    saving()
elif AccType == "current":
    current()
else:
    print("Invalid Query")

