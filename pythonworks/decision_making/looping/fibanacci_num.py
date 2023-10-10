start=10
end=50
for num in range(start,end+1):
    is_prime=True
    for n in range(2,num):
      if(num%n==0):
       is_prime=False
    if(is_prime==True):
      print(num)

