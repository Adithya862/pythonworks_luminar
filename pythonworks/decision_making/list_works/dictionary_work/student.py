student={"roll":100,"name":"ravi","course":"django"}
# print(student["course"]) #[]-calling values
# print(student.get("course")) #get(key)-calling values

# if "total" in student:
#     print("present")
# else:
#     print("not present")

# student["grade"]="A"
# print(student)

for k in student.keys():
    print(k)

# for v in student.values():
#     print(v)

# for k,v in student.items():#-key value written at a time using items()
#     print(k,v)
w="is_vaccinated"
for w in student:
    print("second dose")
else:
     print("first dose")