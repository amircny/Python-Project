class BOOK:
    def __init__(self,name_1,publisher,year,price,shops):

        self.name=name_1
        self.publisher=publisher
        self.year=year
        self.price=price
        self.shops=shops
    def __str__(self):
        return f"name:{self.name},publisher:{self.publisher},Year:{self.year},price:{self.price},shop:{self.shops}"    

class Student:
    def __init__(self,name, age, scores):
      self.name=name
      self.age=age
      self.scores=scores
      self.avg=self.calculate_avg(scores)

    def calculate_avg(self,scores):
     sum_avg=sum(scores)/ len(scores)
     return sum_avg
    
    def add_score(self, new_score):
     self.scores.append(new_score)
     print("Added")
     self.avg=self.calculate_avg(self.scores)


    def __str__(self):
       return f"Name:{self.name},Age:{self.age},Scores:{self.scores},avg:{self.avg}"
    
#................main.............................    
b1=BOOK("Python","p1",2012,30000,["shop1,shop2"])
Student1=Student("s1",18,[12,17,20])
Student1.add_score(30)
print(b1)
print(Student1)
