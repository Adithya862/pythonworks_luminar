def count(val):
   c_count=0
   v_count=0
   for i in range(len(val)):
    if val[i] in("a","e","i","o","u"):
       v_count+=1
    else:
       c_count+=1
    print(v_count)
    print(c_count)
    break 
val=input("enter a name")
count(val)

# find hcf using fn
# lcm
# prime or not
# print even numbers from given list[1,2,3,4,5,6,7,8,9,10]