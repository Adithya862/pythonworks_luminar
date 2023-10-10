#  Ask the user to enter a number between 10 and 20. If they enter a value under 10, display the messag
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

    
