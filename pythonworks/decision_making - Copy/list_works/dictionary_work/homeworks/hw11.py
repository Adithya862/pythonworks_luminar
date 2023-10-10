# 1.Ask how many people the user wants to invite to a party. If they enter a number below 10, ask for the n
# ames and after each name display “[name] has been invited”. If they enter a number which is 10 or highe
# r, display the message “Too many people”

num=int(input("how many people do you want to invite to a party:"))
if(num<10):
  name=input("enter your name")
  print(name,"has been invited")
else:
  print("too many people")


