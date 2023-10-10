colors=["red","green","blue"]
colors.append("yellow")#adding object
print(colors)


colors=["red","green","blue"]
colors.pop(1)#remove 
print(colors)

colors=["red","green","blue"]
colors.sort()#ascending order
print(colors)

colors=["red","green","blue"]
colors.sort(reverse=True)#desecnding order
print(colors)

colors=["red","green","blue","red","green"]
print(colors.count("red"))

colors=["red","green","blue"]
colors.clear()
print(colors)