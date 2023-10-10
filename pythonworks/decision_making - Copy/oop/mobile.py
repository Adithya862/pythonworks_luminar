class Mobile:
  name:str
  color:str
  model:str 
  price:int
  
  def __init__(self,name,color,model,price):
    self.name=name
    self.color=color
    self.model=model
    self.price=price
 
  
  def display_mob(self):
      print(self.name,self.color,self.model,self.price)
  
  obj1=Mobil("oppo","black","F15",20000)