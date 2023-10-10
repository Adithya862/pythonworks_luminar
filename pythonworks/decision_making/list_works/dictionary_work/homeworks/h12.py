# Ask the user to enter a number. Keep asking until they enter a value over 5 and then display the mess
# age “The last number you entered was a [number]” and stop the program
num=0
while(num<=5):
    num=int(input("enter a number:"))
    print("the last number you entered is:",num)
    
