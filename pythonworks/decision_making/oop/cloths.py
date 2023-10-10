class Cloths:
    data=[
        {"id":1,"brand":"Allen solly","color":"red","price":34000,"material":"cotton"},
        {"id":2,"brand":"Adidas","color":"green","price":34000,"material":"cotton"},
        {"id":3,"brand":"H&M","color":"blue","price":34000,"material":"cotton"},
        {"id":4,"brand":"Nike","color":"pink","price":34000,"material":"cotton"},
        {"id":5,"brand":"Zara","color":"Grey","price":34000,"material":"cotton"},
        
          ]
    def get(self,*args,**kwargs):
     return self.data
    
    def retrieve(self,*args,**kwargs):
     id=kwargs.get("id")
     records=[c for c in self.data if c.get("id")==id]
     return records
    
    def create(self,*args,**kwargs):
        self.data.append(kwargs)
    
    def destroy(self,*args,**kwargs):
        id=kwargs.get("id")
        obje=[c for c in self.data if c.get("id")==id].pop()#or [0]
        self.data.remove(obje)

obj=Cloths()
# print(obj.get())

# print(obj.retrieve(id=4))


obj.create(id=6,brand="H&M",color="orange",price=24000)
print(obj.get())


# obj=Cloths()
# obj.destroy(id=4)
# print(obj.get())


