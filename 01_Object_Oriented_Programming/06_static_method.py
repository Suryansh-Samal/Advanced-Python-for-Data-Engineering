class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Hello, this is {self.name}. I am {self.age} years old.")

    @staticmethod
    def add(x,y):
        print(x+y)
        return x+y

human1 = Person("Suryansh", 18)
human1.info()
sum=human1.add(5,10)
print(f"The sum is: {sum}") 
