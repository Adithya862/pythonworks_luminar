def num(num1,num2):
  hcf=1
  for num in range(2,num2+1):
    if(num1%num==0)and(num2%num==0):
     hcf=num
    lcm=int(num1*num2)/hcf
    print(lcm)
num(12,14)