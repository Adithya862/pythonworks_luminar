from  json import load
fread=open("C://Users//hp//Desktop//pythonworks//decision_making//functions1//lambda_function//write//data.txt")
odd_w=open("C://Users//hp//Desktop//pythonworks//decision_making//functions1//lambda_function//write//even.txt","w")
even_w=open("C://Users//hp//Desktop//pythonworks//decision_making//functions1//lambda_function//write//odd.txt","w")
for line in fread:
   num=int(line.rstrip("\n")) #read chyymbm string ila kittuka int lot convert chyynm
   if num%2==0:
       even_w.write(str(num)+"\n")
   else:
       odd_w.write(str(num)+"\n")

 