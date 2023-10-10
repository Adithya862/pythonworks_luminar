# repetition avoid chyynda caseil
# decorators
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @property
    def get_name(self):
        return self.name
obj=Student("adithya","hari")
# print(obj.get_name())#without decorator method ()-use chyynm
print(obj.get_name)