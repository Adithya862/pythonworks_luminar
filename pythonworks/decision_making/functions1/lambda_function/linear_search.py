# linear search
lst=[10,12,13,14,15]
element=13
i=0
limit=len(lst)
is_present=False
while(i<limit):
    cur_val=lst[i]
    if cur_val==element:
     is_present=True
     break
    i+=1
print(is_present)
