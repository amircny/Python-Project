class Student:
    student_number=1000
    def __init__(self,name,age,scores,email):
        self.id=Student.create_id()
        self.name=name
        self.age=age
        self.scores=scores
        self.avg=self.calculate_avg()
        self.email =self.valid_email(email)

    def __str__(self):
        return f"ID:{self.id},Name:{self.name},scores:{self.scores},Age:{self.age},Email:{self.email}"    
    
    def calculate_avg(self):
      result=sum(self.scores)/len(self.scores)
      return result

    @classmethod 
    def create_id(cls):
        s_id="s"+str(cls.student_number)
        cls.student_number+=1
        return s_id
    
    @staticmethod
    def valid_email(email):
        if "@" in email and len(email) > 6 and email.endswith(".com"):
            return email
        return None 

    def update_email(self,new_email):
       self.email=self.valid_email(new_email) or self.email

if __name__ == "__main__":
    st1 = Student("n1", 19, [18, 19], "a.b@gmail.com")
    print(st1)

    st2 = Student("n1", 19, [18, 19], "gmail.com")
    print(st2)