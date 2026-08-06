"""
Topic: Classes and Objects
Description: Demonstrates creating a class, defining methods,
and creating multiple objects.
Author: Suryansh
"""

# ============================================
# Class Definition
# ============================================

class Person:
    """Represents a person."""

    # Class Variables
    first_person = "Suryansh"
    second_person = "Ayush"

    # Instance Method
    def display_info(self):
        """Displays the names stored in the class."""

        print(f"This is {self.first_person}")
        print(f"This is {self.second_person}")

    # Instance Method
    def greet(self):
        """Greets both people."""

        print(f"Hello {self.first_person}! How are you?")
        print(f"Hello {self.second_person}! How are you?")


# ============================================
# Creating Objects
# ============================================

person1 = Person()
person1.display_info()

print()

person2 = Person()
person2.greet()