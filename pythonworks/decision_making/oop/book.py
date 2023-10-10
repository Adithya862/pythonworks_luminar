class Book:
  book_id:int
  title:str
  author:str 
  rating:int 
  price:int
  publisher:str

  def create(self,book_id,title,author,rating,price,publisher):
    self.book_id=book_id
    self.title=title
    self.author=author
    self.rating=rating
    self.price=price
    self.publisher=publisher
    
  def display_book(self):
      print(self.book_id,self.title,self.author,self.rating,self.price,self.publisher)
obj1=Book()
obj1.create(101,"The Alchemist","paulo  Coelho",4.8,200,"DcBooks")
obj1.display_book()
