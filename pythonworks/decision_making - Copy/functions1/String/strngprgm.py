# casefold convert  uppercase into lowercase
# String -sequence of characters
name="Adithya"
print(name.casefold())

name="adithya"
print(name.capitalize())

name="adithya"
print(name.count("a"))

name="adithya"
print(name.startswith("dh"))# True or False

name="adithya"
print(name.endswith("a"))

name="adithya"
print(name.isalpha())#alphabets (a-z) True

name="adithya"
print(name.isdigit())


name="adithya"
print(name.isalnum())#alphabets,number except special characters

name="adithya\n"
print(name.strip("\n")) #remove left and right

name="\nadithya\n"
print(name.strip("\n")) 

name="thedtheuthe"
print(name.rstrip("t")) 

name="adithya"
print(name.lstrip("a")) 

name="adithya"
print(name.index("h")) # written in which position

name="python is a scripting language"
word=name.split(" ")
print(word)



name="python is a scripting language"
words=name.split(" ")
print(words)
for w in words:
    print(w)





