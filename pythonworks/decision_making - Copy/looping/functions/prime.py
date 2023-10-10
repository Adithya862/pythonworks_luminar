def num(num1):
    # if num in [0,1]:
    #      is_prime=False
    # else:
    is_prime=True
    for num in range(2,num1):
      if(num1%num==0):
        is_prime=False
        break
    print(is_prime)
num(6)