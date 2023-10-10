def display_emp(**kwargs):
    print (kwargs)
    print(kwargs.get("name"))

display_emp(name="adithya",dep="it",n_palce="ptm",w_palce="eklm",salary="25000")


# create a function display_student and print student name and course
# display_student(name="ravi",course="django",ro="1000",gender="male")
def display_student(**kwargs):
    print(kwargs)
    print(kwargs.get("name"))
    print(kwargs.get("course"))
# display_student(name="ravi",course="django",rol="1000",gender="male")

