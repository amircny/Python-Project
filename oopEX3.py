#...Project shope Book.....
from queue import Full


class BOOKS:
    def __init__(self,name,price, year, publisher):
     self.name=name
     self.price=price
     self.year=year
     self.publisher=publisher
    def __str__(self):
       return f"name:{self.name},price:{self.price},Year:{self.year},publisher:{self.publisher}"
        
class shops:
    def __init__(self,name):
     self.name=name
     self.products={}
    
    def add_book(self,book):
      if book.name not in self.products:
        self.products[book.name]=book
        print("ADDED")
      else:
        print("EXIST")  
    
    def Dell_book(self,name):
      self.products.pop(name)
      print ("Dell")

    def Search(self,name):
      if self.products != None:
        name_search=self.products.get(name,"Name not found")
        print(name_search)
        sh=input("Would you like Edit?please answe with Yes or No")
        if(sh=="Yes"):
          namee=input("please insert new name")
          #print(namee)
          self.products[name]=namee
          print("Edit")
        else:
          return
        
      else:
        print("It is Empaty")

    
    def __str__(self):
     return f"name:{self.name},products:{self.products}\n,Number of books:{len(self.products)}" 

#......Main...............
b1=BOOKS("b1",200,2020,"p1")
b2=BOOKS("b2",200,2020,"p2")
b3=BOOKS("b3",200,2020,"p3")
b4=BOOKS("b4",200,2020,"p4")
b5=BOOKS("b5",200,2020,"p5")
b6=BOOKS("b6",200,2020,"p6")
sh=shops("sh1")
sh.add_book(b1)
sh.add_book(b2)
sh.add_book(b3)
sh.add_book(b4)
sh.add_book(b5)
sh.add_book(b6)
sh.Search(b6.name)
print(sh)
#sh.Dell_book(b1.name)
#...sh.Dell_book("b1")
#
