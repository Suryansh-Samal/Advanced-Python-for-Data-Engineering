"""
Topic: Encapsulation
Description: Demonstrates public, protected, and private variables in Python.
Author: Suryansh
"""

# ============================================
# Encapsulation
# ============================================

class MyClass:

    # Constructor
    def __init__(self, dyn1, dyn2, dyn3):

        self.dyn1 = dyn1      # Public Variable (Accessible from anywhere)

        self.__dyn2 = dyn2    # Private Variable (Cannot be accessed directly)

        self._dyn3 = dyn3     # Protected Variable (Should be accessed carefully)

    # Method to access the public variable
    def func1(self):
        print(f"Hello World! {self.dyn1}")

    # Method to access the private variable
    def func2(self):
        print(f"Hello Globe! {self.__dyn2}")

    # Method to access the protected variable
    def func3(self):
        print(f"Hello Universe! {self._dyn3}")


# ============================================
# Creating Object
# ============================================

obj = MyClass("US", "India", "Canada")

# Calling methods
obj.func1()
obj.func2()
obj.func3()

# Accessing the protected variable
print(obj._dyn3)

'''
The line below would give an error because
__dyn2 is a private variable.

print(obj.__dyn2)
'''

# Creating a new variable named dyn2
obj.dyn2 = "Ukraine"

'''
This does NOT change the original private variable.
Instead, it creates a new instance variable named dyn2.
'''

print(obj.dyn2)

# The original private variable is still unchanged
obj.func2()