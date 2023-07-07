from student import Student
from student_management_system import StudentManagementSystem

def print_menu():
    print("\n=============Student Management System=============")
    print("1.Add student")
    print("2.Inquire student")
    print("3.Modify student")
    print("4.Delete student")
    print("q.Quit")
    print("\n===================================================")

def get_student_info_from_user():
    student_id=input("Enter student id: ")
    name=input("Enter name: ")
    age=input("Enter age: ")
    return student_id,name,age

sms=StudentManagementSystem()

while True:
    print_menu()
    choice=input("Enter operation number: ")

    if choice=="1":
        student_id,name,age=get_student_info_from_user()
        student=Student(student_id,name,age)
        sms.add_student(student)
    elif choice=="2":
        student_id=input("Enter student id to inquire: ")
        sms.search_student(student_id)
    elif choice=="3":
        ststudent_id=input("Enter student id to modify: ")
        name=input("Enter name to modify: ")
        age=input("Enter age to modify: ")
        sms.update_student(student_id,name,age)
    elif choice=="4":
        student_id=input("Enter student id to delete: ")
        sms.delete_student(student_id)
    elif choice.lower()=="q":
        print("Terminate the program")
        break
    else:
        print("Wrong input. Try again")