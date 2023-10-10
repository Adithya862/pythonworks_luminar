text="sunil gavaskar had a no-hold-barred remark on overseas commentators"
words=(text.split(" "))
vowels=["a","e","i","o","u"]
for w in words:
  # if w.casefold().startswith(vowels):
  #   print(w)
  if w[0].casefold() in vowels:
    print(w)
 
