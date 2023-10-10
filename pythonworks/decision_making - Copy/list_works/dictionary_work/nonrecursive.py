words="ABABBCDCEF"
wc={}
for ch in words:
    if ch in wc:
        wc[ch]+=1  
    else:
        wc[ch]=1
for k,v in wc.items():
        if v==1:
          print(k)