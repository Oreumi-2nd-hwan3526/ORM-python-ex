from student import Student

class StudentManagementSystem:
    def __init__(self):
        self.students=[]

    def add_student(self,student):
        self.students.append(student)
        print("Student info added")
    
    def search_student(self,student_id):
        for student in self.students:
            if student.student_id==student_id:
                return print(student.get_info())
        return "Cannot find the student info"
    
    def delete_student(self,student_id):
        for student in self.students:
            if student.student_id==student_id:
                self.students.remove(student)
                print("Student info deleted")
                return
        return "Cannot find the student info"
    
    def update_student(self,student_id,name,age):
        for student in self.students:
            if student.student_id==student_id:
                student.name=name
                student.age=age                
                print("Student info modified")
                return
        print("Cannot find the student info")