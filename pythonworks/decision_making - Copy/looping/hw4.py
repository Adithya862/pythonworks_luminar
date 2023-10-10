
# fibanacci 
# prev=0
# current=1
# start=1
# print(prev)
# print(current)
# for fib in range(1,9):
#     print(fib)

a=0
b=1
limit=24
print(a)
print(b)
count=1
for i in range(1,24+1):
    c=a+b
    a=b
    b=c
    fib=c
    if fib<=limit:
        print(fib)
    else:     
       break
print("count",count)