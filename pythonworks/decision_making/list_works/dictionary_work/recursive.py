text="ABCDA"
# print first recursive character
wc={}
for ch in text:
   if ch in wc:
      print(ch,"is first recursive")
   else:
      wc[ch]=1

