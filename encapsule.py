class bank_ac:
    def __init__(self,name,balance=2000):
        self.name=name
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
        print("Deposit successful")
    def withdraw(self,amount):
        if self.__balance>=amount:
            self.__balance-=amount
            print("Withdraw successful of",amount)
        else:
            print("Insufficient balance")
    def get_balance(self):
        return self.__balance
acc=bank_ac("John")

acc.withdraw(200)
acc.deposit(500)
print("Balance after deposit:",acc.get_balance())