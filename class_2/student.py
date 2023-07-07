class Student:
    def __init__(self,student_id,name,age):
        self.student_id=student_id
        self.name=name
        self.age=age

    def get_info(self):
        return f"id {self.student_id}, name: {self.name}, age: {self.age}"