class Student:
  rollno:int
  name:str
  gender:str 
  dob:int 
  age:int
  address:str
  

  def __init__(self,roll_no,name,gender,dob,age,address):
    self.rollno=roll_no
    self.name=name
    self.gender=gender
    self.dob=dob
    self.age=age
    self.address=address
    
    
  def display_stu(self):
    print(self.rollno,self.name,self.gender,self.dob,self.age,self.address)

  def __str__(self):#object string representation
    return self.name
obj=Student(1,"Adithya","Female","11-11-2002",20,"aaaa")
# #obj.create(1,"Adithya","female",11-11-2002,20,"aaaaa",7902957789)without constructor
# obj.display_stu()
print(obj)