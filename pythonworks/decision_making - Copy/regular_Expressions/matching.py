# from re import*
# text="ababababcab"
# matcher=finditer("ab",text)
# for m in matcher:
#     print(m.start(),m.group())


# from re import*
# text="ababababcab"
# matcher=finditer("ab",text)
# count=0
# for m in matcher:
#     print(m.start(),m.group())
#     count+=1
# print(count)



# from re import*
# text="ababcd097c"
# pattern="[0-9]"
# matcher=finditer(pattern,text)
# for m in matcher:
#  print(m.start(),m.group())


# from re import*
# text="ababcd097c"
# pattern="[a-z]"
# matcher=finditer(pattern,text)
# for m in matcher:
#  print(m.start(),m.group())


# from re import*
# text="ababcdABCD097c"
# pattern="[A-Z]"
# matcher=finditer(pattern,text)
# for m in matcher:
#  print(m.start(),m.group())

# from re import*
# text="ababcdABCD097c"
# pattern="[a-zA-Z]"
# matcher=finditer(pattern,text)
# for m in matcher:
#  print(m.start(),m.group())



# from re import*
# text="ababcdABCD097c_*"#spcl character print avilla
# pattern="[a-b0-9]"
# matcher=finditer(pattern,text)
# for m in matcher:
#  print(m.start(),m.group())


# from re import*
# text="ababcdABCD097c_*"#spcl character print avilla
# pattern="[a-b0-9]"
# matcher=finditer(pattern,text)
# for m in matcher:
#  print(m.start(),m.group())

# from re import*
# text="ababcdABCD097c_*"#spcl character print avilla
# pattern="[^0-9]"# ^-except
# matcher=finditer(pattern,text)
# for m in matcher:
#  print(m.start(),m.group())

# from re import*
# text="asdfEghOki".casefold()
# pattern="[aeiou]"#[aeiouAEIOU]
# matcher=finditer(pattern,text)
# for m in matcher:
#  print(m.start(),m.group())


# from re import*
# text="asd4fEgh#@$Oki".casefold()
# pattern="[b-df-hj-np-tv-z]"#"[^aeiou]"
# matcher=finditer(pattern,text)
# for m in matcher:
#  if m.group().isalpha():
#    print(m.group())


from re import*
text="asdfEgh987*$Oki".casefold()
pattern="[^aeiou\W\d]" #_ is not a special character
matcher=finditer(pattern,text)
for m in matcher:
 print(m.start(),m.group())
