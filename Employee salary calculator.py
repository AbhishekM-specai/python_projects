#Employee salary calculator
'''
class Employee:
    def __init__(self, name,emp_id,basic_salary):
        self.name = name
        self.emp_id = emp_id
        self.basic_salary = basic_salary
        self.da=0
        self.hra=0

    def cal_DA(self,da_percentage):
        self.da= (self.basic_salary * da_percentage) / 100
        print("your Dearness allowance is:",self.da)

    def cal_HRA(self,hra_amount):
        self.hra= hra_amount
        print("your HRA  is:",self.hra)

    def total_salary(self):
        total=self.basic_salary+self.hra+self.da
        print("your Total Salary is:",total)



a=Employee(input("Enter the employee name:"),
           int(input("Enter the employee id:")),
           int(input("Enter the basic salary:")))
a.cal_DA(float(input("Enter your DA  percentage:")))
a.cal_HRA(int(input("Enter your actual HRA amount:")))
a.total_salary()
'''''