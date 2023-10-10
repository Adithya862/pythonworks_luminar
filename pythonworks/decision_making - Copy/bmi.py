# height_incm=165
height_incm=int(input("enter the height in cm"))
# weight_inkg=25
weight_inkg=int(input("enter the height in cm"))
height_inmeter=height_incm/100
bmi=weight_inkg/(height_inmeter)**2
print(bmi)
if(bmi<=19):
  print("underweight")
elif(bmi<=25):
  print("normal weight")
elif(bmi<=30):
  print("over weight")
else:
  print("obesity")
  
  
