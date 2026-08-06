"""
Topic: Class Methods
Description: Demonstrates the use of @classmethod to modify a class variable.
Author: Suryansh
"""

# ============================================
# Employee Class
# ============================================

class Employee:

    # Class Variable
    company = "Apple"

    # Constructor
    def __init__(self, emp_name, emp_dept:str):
        self.emp_name = emp_name
        self.emp_dept = emp_dept

    # Method to display employee information
    def info(self):
        print(f"Hello, this is {self.emp_name}. I work for the {self.emp_dept} department at {self.company}")

    # Class Method
    @classmethod
    def change(cls, company_new_name):
        """
        Changes the value of the class variable.
        """
        cls.company = company_new_name


# ============================================
# Creating Objects
# ============================================

obj = Employee("Suryansh", "Data Engineering")
obj.info()

obj2 = Employee("Naman", "Marketing")
obj2.info()

# Changing the class variable
obj.change("Google")

print("\nAfter changing the company name:")

obj.info()
obj2.info()
