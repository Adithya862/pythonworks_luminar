# Ask the user to enter 5 numbers and find the average using for or while loop.
total_sum=0
for n in range(5):
    num1=int(input("enter a number"))
    total_sum=total_sum+num1
    avg=total_sum/5
print("average =",avg)