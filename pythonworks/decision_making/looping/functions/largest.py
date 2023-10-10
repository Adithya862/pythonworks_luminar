# a=int(input("enter  num1"))   
# b=int(input("enter  num2"))
# c=int(input("enter num3")) 
def largest(a,b,c):
  if(a>b)and(a>c):
    print("a is largest",a)
  elif(b>a)and(b>c):
    print("b is greater",b)
  else:
   print("c is greater",c)
largest(2,3,4)