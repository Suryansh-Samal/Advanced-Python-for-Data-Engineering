class Person:

  var1 = "Suryansh"
  var2= 'Ayush'

  def info(self):
    print(f'This is {self.var1}')
    print(f'This is {self.var2}')

  def greet(self):
    print(f'Hello {self.var1}! How are you?') 
    print(f'Hello {self.var2}! How are you?') 
obj = Person()
obj.info()
obj2 = Person()
obj2.greet()
    