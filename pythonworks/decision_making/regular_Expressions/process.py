from re import*
f=open("C:\\Users\\hp\\Desktop\\pythonworks\\decision_making\\regular_Expressions\\data.text","r")
phone_rule="\d{10}"
mail_rule="[\w]+@gmail.com"
mail_ids=[] 
phone_numbers=[]
for line in f:
 word=(line.rstrip("\n").split())
 for w in word:
   matcher=fullmatch(phone_rule,w)
   email_matcher=fullmatch(mail_rule,w)
   if matcher!=None:
    phone_numbers.append(w)
   elif email_matcher!=None:
     mail_ids.append(w)
     
print(phone_numbers)
print(mail_ids)





