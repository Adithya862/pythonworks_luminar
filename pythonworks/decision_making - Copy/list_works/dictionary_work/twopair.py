lst=[2,3,4,5,7]
lst.sort()
sum=9
low=0
upper=len(lst)-1
while(low<upper):
    current_sum=lst[low]+lst[upper]
    if current_sum==sum:
        print("pair",lst[low],lst[upper])
        break
    elif(current_sum<sum):
        low+=1
    else:
        upper-=1

lst=[2,3,4,5,7]
lst.sort()
sum=9
low=0
upper=len(lst)-1
while(low<upper):
    current_sum=lst[low]+lst[upper]
    if current_sum==sum:
        print("pair",lst[low],lst[upper])
        low+=1
    elif(current_sum<sum):
        low+=1
    else:
        upper-=1