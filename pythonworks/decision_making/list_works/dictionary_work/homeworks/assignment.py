1.# Ask the user to enter a number between 10 and 20 (inclusive). If they enter a number within this range,
# display the message “Thank you”, otherwise display the message “Incorrect 
# answer”
num=int(input("enter a number"))
if(num>=10 and num<=20):
   print("thank you")
else:
   print("incorrect")
   
2.# Ask the user to enter a number between 10 and 20 (inclusive). If they enter a number within this range,
# display the message “Thank you”, otherwise display the message “Incorrect 
# answer”
num=int(input("enter a number"))
if num<=10:
    print("too low")
elif(num>=10 and num<=20):
     print("correct")
else:
    print("too high")

3.# Ask the user’s age. If they are 18 or over, display the message “You can vote”, if they are aged 17, disp
# lay the message “You can learn to drive”, if they are 16, display the message“You can buy a lott
# ery ticket”,if they are under 16, display the message “You can go for treat”. 
age=int(input("enter your age"))
if(age>=18):
    print("you can vote")
elif(age==17):
    print("you can learn to drive")
elif(age==16):
    print("you can buy a lottery ticket")
elif(age<=16):
    print("you can go for treat")


4.# Ask the user to enter 1, 2 or 3. If they enter a 1, display the message “Thank you”, if they enter a 2, disp
# lay “Well done”, if they enter a 3, display “Correct”. If they enter anything else, display “Error message”. 
num=int(input("enter a number"))
if(num==1):
    print("thank you")
elif(num==2):
    print("well done")
elif(num==3):
    print("correct")
else:
    print("error message")

5.# Write a programto whether a number(from user)is divisible by 2 and 3 both.
num=int(input("enter a number"))
if(num%2==0 and num%3==0):
    print("divisble by 2")
elif(num%3==0):
    print("divisble by 3")
else:
    print("not divisible")


6.# Write a program to check whether the character is vowel or not. 
text=input("enter a character")
vowels= ["a","e","i","o","u"]
if text in vowels:
    print("vowel")
else:
    print("not vowel")


7.# Write a program to check whether the character is vowel or not. 
num=int(input("enter a number"))
for i in range(0,11):
    print(num,"*",i,"=",num*i)


8.# Python program to print all the even numbers within the given range. 
n1=int(input("enter a number1"))
n2=int(input("enter a number2"))
for n in range(n1,n2):
    if(n%2==0):
        print(n)

9.# Ask the user to enter their name and then display their name three times.
text=input("enter your name")
for i in range(3):
 print(text)

10.# Ask the user to enter their name and a number. If the number is less than 10, then display their name t
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
 
11.# 1.Ask how many people the user wants to invite to a party. If they enter a number below 10, ask for the n
# ames and after each name display “[name] has been invited”. If they enter a number which is 10 or highe
# r, display the message “Too many people”

num=int(input("how many people do you want to invite to a party:"))
if(num<10):
  name=input("enter your name")
  print(name,"has been invited")
else:
  print("too many people")

12.# Ask the user to enter a number. Keep asking until they enter a value over 5 and then display the mess
# age “The last number you entered was a [number]” and stop the program
num=0
while(num<=5):
    num=int(input("enter a number:"))
    print("the last number you entered is:",num)
    
13.#  Ask the user to enter a number between 10 and 20. If they enter a value under 10, display the messag
#  e “Too low” and ask them to try again. If they enter a value above 20, display the message “Too high” and
#  ask them to try again. Keep repeating this until they enter a value that is between 10 and 20 and then dis
# play the message “Thank you”. 

while(True):
 count=int(input("enter a number"))
 if(count<=10):
    print("Too low. try again!")
 elif(count>=20):
    print("Too high. try again!")
 else:
    print("Thank you") 
    break

14.# write a program to print the series 10,20,30,...300 using for loop
num1=10
num2=300
for n in range(num1,num2+1,10):
    print(n)
    
   
15.# Ask the user to enter 5 numbers and find the average using for or while loop.
total_sum=0
for n in range(5):
    num1=int(input("enter a number"))
    total_sum=total_sum+num1
    avg=total_sum/5
print("average =",avg)