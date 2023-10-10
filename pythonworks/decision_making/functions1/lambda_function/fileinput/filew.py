f_read=open("C:\\Users\\hp\\Desktop\\pythonworks\\decision_making\\functions1\\lambda_function\\fileinput data.txt","w")
f_odd=open("C:\\Users\\hp\\Desktop\\pythonworks\\decision_making\\functions1\\lambda_function\\fileinput odd.txt","w")
f_even=open("C:\\Users\\hp\\Desktop\\pythonworks\\decision_making\\functions1\\lambda_function\\fileinput even.txt","w")
for line in f_read:
    num=int(line.rstrip("\n"))
    if num%2==0:
        f_odd.write(str(num)+"\n")
    else:
        f_even.write(str(num)+"\n")