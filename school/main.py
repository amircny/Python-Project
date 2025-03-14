from university import *

def create_student_objevt():
    name = input("student name: ")
    age = int(input("student age: "))
    number = int(input("number of your scores: "))
    scores = []
    for i in range(number):
        score = float(input(f"score_{i}: "))
        scores.append(score)
    email = input("student email: ")
    str1= Student(name, age, scores,email)
    return str1

def get_edit_data():
    id_ = input("id fore edit: ")
    new_name = input("new name or blank to ignore: ")
    new_age = input("new age or blank to ingone: ") 
    new_email = input("new email or blank to ignore: ")
    return id_, new_name, new_age, new_email

def main():
    u1 = University("u1", 1990)
    while True:
        cmd = input("add, remove, display, edit: ")
        if cmd == "add":
            str1 = create_student_objevt()
            u1.add_student(str1)

        elif cmd == "remove":
            id_ = input("id to remove: ")
            u1.dell_student(id_)

        elif cmd == "display":
            u1.display()

        elif cmd == "edit":
            u1.display()
            id_, new_name, new_age, new_email = get_edit_data()
            u1.edit(id_, new_name, new_age, new_email)

        elif cmd == "":
            continue

        elif cmd == "exit":
            break

        else:
            print("Not Found!")

if __name__ == "__main__":
    main()