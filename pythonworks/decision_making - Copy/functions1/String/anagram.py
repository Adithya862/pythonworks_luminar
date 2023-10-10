text="fast"
out="fats"
wrd_srt1=sorted(text)
wrd_srt2=sorted(out)
print(wrd_srt1)
print(wrd_srt2)
if wrd_srt1==wrd_srt2:
    print("anagram")
else:
    print("not")