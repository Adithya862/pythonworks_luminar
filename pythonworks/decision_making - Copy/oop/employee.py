class Employee:
    data=[
        {"id":1,"name":"jhon","dept":"hr","salary":34000},
        {"id":2,"name":"hari","dept":"it","salary":24000},
        {"id":3,"name":"ravi","dept":"qa","salary":64000},
        {"id":4,"name":"vijay","dept":"hr","salary":74000},
        {"id":5,"name":"tom","dept":"it","salary":24000},
        {"id":6,"name":"vipin","dept":"qa","salary":14000},
        
    ]

    # return all employee records list
    # employee details
    # add employee
    # edit
    # delete
    def get(self,*args,**kwargs):#class nu akath anel mathram self kodutha mathi
        return self.data
    def retrieve(self,*args,**kwargs):#id veche retrieve chyyan pattu name vech pattilla
        id=kwargs.get("id")
        records=[emp for emp in self.data if emp.get("id")==id]
        return records
    def create(self,*args,**kwargs):
        self.data.append(kwargs)
    
    def destroy(self,*args,**kwargs):
        id=kwargs.get("id")
        obje=[e for e in self.data if e.get("id")==id].pop()#or [0]
        self.data.remove(obje)
    def update(self,id=None,*args,**kwargs):
        id=id
        obje=[emp for emp in self.data if emp.get("id")==id][0]
        print(obj)
        obje.update(kwargs)
        print("employee object updated")

# obj=Employee()
# obj.destroy(id=4)

# print(obj.get())

# print(obj.retrieve(id=3))


# obj.create(id=7,name="vishnu",dept="hr",salary=24000)
# print(obj.get())

obj=Employee()
obj.update(id=1,salary="24000")
obj.update(id=4,name="hari",salary="24000")
print(obj.retrieve(id=4))