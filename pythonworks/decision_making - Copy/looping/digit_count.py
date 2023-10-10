number=372
# int(input)
orginal=number
sum=0
digit_count=len(str(number))
while(number!=0):
   last_digit=number%10
   exponent=last_digit**digit_count
   sum=sum+exponent
   number=number//10
print("number is armstrong" if sum==orginal else "number is not armstrong")
