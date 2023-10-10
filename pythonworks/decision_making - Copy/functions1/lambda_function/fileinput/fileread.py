f=open("C:\\Users\\hp\Desktop\\pythonworks\\decision_making\\functions1\\lambda_function\\fileinput\\data.txt","r")
lst=[]
# for  line in f:
    # print(line)

for  line in f:
    lst.append(line.rstrip("\n"))
print(lst)
long_word=max(lst,key=lambda w:len(w))
print(long_word)
