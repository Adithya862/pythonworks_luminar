from re import*
vechile_number=input("enter  vechile number")
rule="(KL)-\d{2}-[A-Z]-{1,2}-\d{4}"
matcher=fullmatch(rule,vechile_number)
print("invalid" if matcher==None else "valid")
