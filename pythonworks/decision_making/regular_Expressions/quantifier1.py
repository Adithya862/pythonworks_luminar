# starting with an alphabet k,l,m
#  second place must be a digit and that digit must be / by 3
# followed by any number of character

from re import*
variable=input("enter  variable name")
rule="[k-m][369][\w]*"
matcher=fullmatch(rule,variable)
print("invalid" if matcher==None else "valid")
