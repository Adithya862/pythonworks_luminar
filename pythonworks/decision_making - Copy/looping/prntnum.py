# print all numbers from 1 to 50 if num/by 3 print"a" if num/by 5"cd" if num/15"efg" else print that number
start=1
end=50
while(start<=50):
  if(start%3==0): 
    print("f") 
  elif(start%5==0):
    print("cd")
  elif(start%15==0):
    print("efg")
  else:
    print(start)
  start+=1
