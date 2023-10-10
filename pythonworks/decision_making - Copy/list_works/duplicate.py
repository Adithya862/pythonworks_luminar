lst=[2,1,5,3,6,3]
    # print duplicate numbers
lst.sort()
for i in range(0,len(lst)-1):
    current=lst[i]
    next=lst[i+1]

    # diff=next-current
    # if diff==0:
    #  print("duplicate value",current)
    #  break

    if current==next:
        print(current)
