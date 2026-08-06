class Company:

    def __init__(self, company_name):
        self.company_name = company_name

    def company_info(self):
        return f'{self.company_name}'

class Department:

    def __init__(self, department_name):
        self.department_name = department_name

    def department_info(self):
        return f'{self.department_name}'

class Employee(Company, Department):

    def __init__(self,employee_name:str, department_name:str, company_name:str):
       self.employee_name = employee_name
       Department.__init__(self, department_name)
       Company.__init__(self, company_name)

    def employee_info(self):
        company = Company.company_info(self)
        department = Department.department_info(self)
        print(f'Employee: {self.employee_name}\nDepartment: {department}\nCompany: {company}')

emp1 = Employee('Suryansh', 'Data', 'Apple')
emp1.employee_info()
