class account:
    def __init__(self , bal , account_no):
        self.bal = bal
        self.account_no = account_no

    def dabit(self , amount):
        self.bal -= amount
        print('Rs.',amount , "was dabited")
        print("total balance",self.get_bal())

    def credit(self , amount):
        self.bal += amount
        print('Rs.',amount , "craditid")
        print("total balance", self.get_bal())

    def get_bal(self):
        return self.bal

acc1 = account(10000, 1344266)
acc1.dabit(1000)
acc1.credit(2000)
acc1.credit(5000)
print("balance is :",  acc1.bal)
print("account no. is :",acc1.account_no)