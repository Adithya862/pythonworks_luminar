lst=[1,2,4,5,7,5,8,5]
lst.sort()
duplicate_list=[]
for i in range(0,len(lst)-1):
    current=lst[i]
    next=lst[i+1]
    if current==next:
        if current not in duplicate_list:
            duplicate_list.append(current)
print(duplicate_list)