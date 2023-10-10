words="ABBCDEC"
wc={}      #0,1-indexing
dup_list=[]#B,C
for ch in words:
    if ch in wc:
        dup_list.append(ch)
    else:
        wc[ch]=1
print(dup_list[0])

