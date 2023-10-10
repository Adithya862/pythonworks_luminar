text="hello hai hello hai"
word=text.split(" ")
wc={}#empty dic
for w in word:
   if w in wc:
    wc[w]+=1
   else:
     wc[w]=1#already olla value
print(wc)
