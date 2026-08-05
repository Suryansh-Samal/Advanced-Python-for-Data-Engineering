class Company:

    def __init__(self,Comp_Name):
        self.Comp_Name = Comp_Name

    def Comp_info(self):
        print(f'Company {self.Comp_Name}')
        return f'Company {self.Comp_Name}'

class Employee(Company):

    def __init__(self, Emp_Name, Comp_Name):
      self.Emp_Name = Emp_Name
      Company.__init__(self,Comp_Name)

    def info (self):
        response= Company.Comp_info(self)
        print(f'Employee {self.Emp_Name} works for {response}')

    def emp_company(self):
        Company.Comp_info(self)

emp1 = Employee('Suryansh' , 'Apple')
emp1.info()
emp1.Comp_info()
emp1.emp_company()

