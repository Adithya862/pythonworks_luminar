expenses=[12000,13000,14000,15000,20000,22000]

# expenses of feb month
# print(expenses[1])

# for e in expenses:
#     print(e)

# for e in expenses:
#     if e >15000:
#         print(e)

# total expenses
# total=0
# for e in expenses:
#     total=total+e
#     print(total)

# highest expenses
# max=0
# for e in expenses:
#     if e>max:
#       max=e
# print(max)


# cheapest price
# min=expenses[0]
# for e in expenses:
#     if e<min:
#       min=e
# print(min)
# or
# print(min(expenses))
min_exp=min(expenses)
print(min_exp)

max_exp=max(expenses)
print(max_exp)

totalsum=sum(expenses)
print(totalsum)