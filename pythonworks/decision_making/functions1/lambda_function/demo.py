sub=lambda n1,n2:n1-n2
print(sub(10,2))

cube=lambda n:n**3
print(cube(3))

max_two=lambda n1,n2:n1 if n1>n2 else n2
print(max_two(10,20))

odd_even=lambda n: "even"if n%2==0 else "odd"
print(odd_even(10))

get_len=lambda w:len(w)
print(get_len("hello"))

# smart_sub
smart_sub=lambda n1,n2:n1-n2 if n1>n2 else n2-n1
print(smart_sub(5,8))