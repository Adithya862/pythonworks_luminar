# def Product(*args):
#  res=1
#  for n in args:
#   res*=n
#   return res
# print(Product(1,2,3,4,5))

def max_word(*args):
    lengthy_word=max(args,key=lambda w:len(w))
    return lengthy_word
print(max_word("hello","good morning","evening"))