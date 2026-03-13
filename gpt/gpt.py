class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def get_info(self):
        return(f"Name: {self.name}, Marks: {self.marks}")

    
    def is_pass(self):
        if self.marks >= 40:
            return True
        else:
            return False


    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75 and self.marks <= 89:
            return "B"
        elif self.marks >= 60 and self.marks <= 74:
            return "C"
        elif self.marks >= 40 and self.marks <= 59:
            return "D"
        else:
           return "F"

name = input("Enter your name: ")
marks = int(input("Enter marks: "))

s1 = Student(name,marks)

print(s1.get_info())
print(s1.is_pass())
print(s1.get_grade())