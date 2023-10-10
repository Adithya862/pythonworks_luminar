text="asdfghjklpoiuytrewqzxcvbnm"
c_count=0
v_count=0
for ch in text:
    if ch in ["a","e","i","o","u"]:
     v_count+=1
    else:
     c_count+=1

print("vowels",v_count) 
print("constants",c_count)       



# # space consonant
# text="aehgt .io"
# c_count=0
# v_count=0
# for ch in text:
#     if ch in ["a","e","i","o","u"]:
#      v_count+=1
#     # elif ch!=" ":
#     elif ch !=" " ".":
#      c_count+=1

# print("vowels",v_count) 
# print("constants",c_count)       
    