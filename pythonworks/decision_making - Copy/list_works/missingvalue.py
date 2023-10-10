lst=[2,4,1,5]
lst.sort()
for i in range(0,len(lst)):
#     diff=lst[i+1] 
# print(lst)
    current=lst[i]
    next=lst[i+1]
    diff=next-current
    if diff!=1:
     print("missing value",current+1)
     break

    lst=[2,1,5,3,6,3]
    # print duplicate numbers