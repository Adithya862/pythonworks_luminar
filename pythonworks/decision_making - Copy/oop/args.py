class Calculator:
    def add(self,*args):
        return sum(args)
obj=Calculator()
print(obj.add(1,5,8,7))