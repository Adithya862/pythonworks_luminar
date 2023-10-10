from re import *
pan_number=input("enter  pan_card number:>")
rule="[A-Z]{3}[PCHFAT]{1}[A-Z]{1}[\d]{4}[A-Z]{1}"
matcher=fullmatch(rule,pan_number)
print("invalid" if matcher==None else "valid")