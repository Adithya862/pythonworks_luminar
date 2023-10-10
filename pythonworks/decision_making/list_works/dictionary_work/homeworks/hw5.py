# Write a programto whether a number(from user)is divisible by 2 and 3 both.
num=int(input("enter a number"))
if(num%2==0 and num%3==0):
    print("divisble by 2")
elif(num%3==0):
    print("divisble by 3")
else:
    print("not divisible")
