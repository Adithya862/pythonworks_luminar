from re import*
text="aabbcaabcaaa"
# pattern="a+"# one or more occurrence of a(minimum one alum vnm maximum athra vnmlum pattum)
# pattern="a*" #zero or more occurence
pattern="a?"
matcher=finditer(pattern,text)
for m in matcher:
    print(m.group(),m.start())

from re import*
phone=input("enter phone number")
rule="\d{10}"
matcher=fullmatch(rule,phone)
if matcher==None:
    print("invalid")
else:
    print("valid")