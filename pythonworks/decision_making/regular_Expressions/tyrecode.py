# 3digit/2digitR2digit/min2 max3 digit alphabet
from re import*
tyre_code=input("enter  Tyre code:")
rule="\d{3}/[\d]{2}[R]\d{2}/[\d]{2,3}[A-Z]"
matcher=fullmatch(rule,tyre_code)
print("invalid" if matcher==None else "valid")
