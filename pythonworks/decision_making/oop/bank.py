from datetime import datetime
class Bank:
    bank_name:str
    acno:int
    person_name:str
    ac_type:str
    balance:int
    def create(self,b_name,a_no,p_name,ac_type,bal):
        self.bank_name=b_name#current object ne point chyyan
        self.acno=a_no
        self.person_name=p_name
        self.ac_type=ac_type
        self.balance=bal
    def deposit(self,amount):
        self.balance+=amount
        print(f"your {self.bank_name} has been credited {amount} avl bal is {self.balance}")
    def Withdrawal(self,amount):
        if amount>self.balance:
         print("transaction failed insufficently")
        else:
            self.balance-=amount
        print(f"your {self.bank_name} has been dedited {amount} avl bal is {self.balance}")
    def get_balance(self):
        print(f"your {self.bank_name}a/c {self.ac_type} bal on is {datetime.today()} is {self.balance}")
obj1=Bank()
obj1.create("sbi",123456,"vijay","saving",4000)

obj1.deposit(2000)
obj1.Withdrawal(1000)
obj1.get_balance()
obj2=Bank()
obj2.create("sbi",123458,"jhon","saving",5000)


