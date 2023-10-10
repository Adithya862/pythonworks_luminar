f=open("C:\\Users\\hp\Desktop\\pythonworks\\decision_making\\functions1\\lambda_function\\fileinput\\numbers.txt","r")
numbers=[line.rstrip("\n") for line in f]
# print(numbers)


# kl vehicle numbers
kerala_num=[n for n in numbers if n.startswith("kl")]
print(kerala_num)