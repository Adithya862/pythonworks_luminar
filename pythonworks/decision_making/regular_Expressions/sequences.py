# from re import*
# text="afgt123$%"
# # pattern="\d" #[0-9]==\d
# # pattern="\D" #[^0-9] except digit
# # pattern="\w"#all alpanumeric character
# pattern="\W"#specail characters
# matcher=finditer(pattern,text)
# for m in matcher:
#  print(m.group(),m.start())

from re import*
variable=input("enter a variable>:")
rule="[a-zA-Z][\w_]"
matcher=fullmatch(rule,variable)
print("valid" if matcher!=None else "invalid")