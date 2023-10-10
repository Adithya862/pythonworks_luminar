# 3 digitbarmstrong number
# num=370
# orginal=num#orginal=37
# # o/p=36(1**3+2**3+3**3)
# sum=0
# while(num!=0):
#     last_digit=num%10
#     cube=last_digit**3
#     sum=sum+cube
#     num=num//10
# if(orginal==sum):
#     print("the number is armstrong")
# else:
#     print("the number is not armstrong")

 # **4-4digit
#   sum=sum+cube
num=1654
orginal=num
sum=0
while(num!=0):
    last_digit=num%10
    cube=last_digit**4
    sum=sum+cube
    num=num//10
if(orginal==sum):
    print("the number is armstrong")
else:
    print("the number is not armstrong")