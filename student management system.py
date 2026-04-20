#student management system
''''
class Student:
    def __init__(self, name,roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_details(self):
        print("Name:", self.name,"\n" "roll_no:", self.roll_no,"\n" "marks:", self.marks)

    def calculate_grade(self):
        if self.marks >= 75:
            return "Grade: A"
        elif self.marks >= 50:
            return "Grade: B"
        elif self.marks >= 35:
            return "Grade: C"
        else:
            return "Failed! work hard."



a=Student(name=input("Enter Name: "),
        roll_no=int(input("Enter Roll No: ")),
        marks=int(input("Enter Marks: ")))
a.display_details()
print(a.calculate_grade())



b=Student(name=input("Enter Name: "),
        roll_no=int(input("Enter Roll No: ")),
        marks=int(input("Enter Marks: ")))
b.display_details()
print(b.calculate_grade())

'''''
