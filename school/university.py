from student import *
class University:
    def __init__(self,name,year):
        self.name=name    
        self.year=year
        self.students={}

    def add_student(self,student):
        self.students[student.id]=student

    def dell_student(self,IDd):
        if IDd in self.students:
            self.students.pop(IDd)
            print("Dell") 
        else:
            print("Not in") 

    def edit(self,id_,New_name,New_age,New_email):
        if id_ in self.students:
           student_=self.students[id_]
           student_.name=New_name or student_.name
           student_.age = New_age or student_.age
           student_.email = Student.update_email(New_email) or student_.email
           print("Edit")
        else:
            print(f"{id_} Not found")
              
    def display(self):
        info = ""
        for st in self.students.values():
            info += str(st)
            info += "\n"
        print(info)

    def __str__(self):
        """info = ""
        for i in self.students.values(): 
            info += str(i)"""
        return f"Name:{self.name},year:{self.year},Student:{len(self.students)} "
