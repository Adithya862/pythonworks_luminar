# num=14
# if num>=10 and num<=20:
#     print("thank you")
# else:
#     print("incorrect")

# num=int(input("enter number"))
# if num<10:
#     print("too low")
# elif(num<=20):
#     print("correct")
# else:
#     print("too high")
    
# age=int(input("enter your age"))
# if age>=18:
#     print("you can vote")
# elif age==17:
#     print("u can lrn drv")
# elif age==16:
#     print("you can by lottery ticket")
# elif age<16:
#     print("you can go for treat")
for row in range(1,7):
    for spc in range(7-row,1,-1):
       print(end=" ")
    for st in range(row):
       print("*",end=" ")
    print()

