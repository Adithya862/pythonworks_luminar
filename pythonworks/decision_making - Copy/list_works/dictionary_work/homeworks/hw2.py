# Ask the user to enter a number between 10 and 20 (inclusive). If they enter a number within this range,
# display the message “Thank you”, otherwise display the message “Incorrect 
# answer”
num=int(input("enter a number"))
if num<=10:
    print("too low")
elif(num>=10 and num<=20):
     print("correct")
else:
    print("too high")



