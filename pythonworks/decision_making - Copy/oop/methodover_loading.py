# method overloading()
class Calculator:
    def add(self,n1,n2):
        return n1+n2
    def add(self,n1,n2,n3):
        return n1+n2+n3
    def add(self,n1,n2,n3):
        return n1+n2+n3
    
obj=Calculator()
print(obj.add(100,120))
    
# function overloading
def add(self,n1,n2):
        return n1+n2
def add(self,n1,n2,n3):
        return n1+n2+n3
def add(self,n1,n2,n3,n4):
        return n1+n2+n3+n4