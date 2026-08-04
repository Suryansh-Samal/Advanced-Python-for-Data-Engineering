"""
Topic: Constructors
Description: Demonstrates constructors, class variables, instance variables, and methods.
Author: Suryansh
"""

# ============================================
# Employee Class
# ============================================

class Employee:

    # Class Variables (Shared by all objects)
    CEO = "Tim Cook"
    Company = "Apple"

    # Constructor
    def __init__(self, emp_name, emp_dept):

        # Instance Variables (Unique for every object)
        self.emp_name = emp_name
        self.emp_dept = emp_dept

    # Method to display employee information
    def info(self):
        print(f"Employee {self.emp_name} works for {self.emp_dept} department at {self.Company}")

    # Method to display CEO information
    def CEO_info(self):
        print(f"{Employee.CEO} is the CEO of the company {self.Company}")

        '''
        We can use both the class name and self
        to access class variables.
        '''


# ============================================
# Creating Objects
# ============================================

obj = Employee("Suryansh", "Data")      # Creating the first object
obj.info()                              # Calling the info method

obj2 = Employee("Arnav", "Marketing")   # Creating the second object
obj2.info()

# Changing the company only for obj2
obj2.Company = "Notion"
obj2.info()

# Calling methods using the class name
Employee.info(obj)
Employee.CEO_info(obj)