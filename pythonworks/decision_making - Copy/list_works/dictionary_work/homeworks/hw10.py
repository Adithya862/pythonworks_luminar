# Ask the user to enter their name and a number. If the number is less than 10, then display their name t
# hat number of times; otherwise display the message “Too high”
txt=(input("enter your name "))
num=int(input("enter a number"))
txt==num
for t in range(num):
 if(num<10):
   print(txt)
 elif(num>=10):
   print("Too high")
   break