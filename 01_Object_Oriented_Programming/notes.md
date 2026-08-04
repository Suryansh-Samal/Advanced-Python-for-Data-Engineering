# Object-Oriented Programming (OOP)

## Topics Covered

- Classes and Objects
- Constructors
- Class Variables
- Instance Variables
- Instance Methods
- Encapsulation
- Data Extraction using Pandas
- Class Methods

---

# 1. Classes and Objects

## Class

A class is a blueprint used to create objects.

```python
class Person:
    pass
```

---

## Object

An object is an instance of a class.

```python
obj = Person()
```

---

## Methods

Methods are functions defined inside a class.

```python
class Person:

    def greet(self):
        print("Hello")
```

Call a method using an object.

```python
obj.greet()
```

---

# 2. Constructors

## What is a Constructor?

A constructor is a special method that is automatically called whenever an object is created.

```python
def __init__(self, emp_name, emp_dept):
```

Its purpose is to initialize the object's data.

---

## Example

```python
class Employee:

    def __init__(self, emp_name, emp_dept):
        self.emp_name = emp_name
        self.emp_dept = emp_dept
```

---

# 3. Class Variables

Class variables are shared among all objects.

```python
class Employee:

    Company = "Apple"
```

They can be accessed using

```python
self.Company
```

or

```python
Employee.Company
```

---

# 4. Instance Variables

Instance variables belong to a specific object.

```python
self.emp_name = emp_name
```

Every object has its own copy.

Example

```python
obj1.emp_name
obj2.emp_name
```

Both objects can have different values.

---

# 5. Instance Methods

Methods are functions written inside a class.

```python
def info(self):
    print(self.emp_name)
```

Call them using

```python
obj.info()
```

or

```python
Employee.info(obj)
```

---

# 6. Encapsulation

Encapsulation means restricting direct access to data and controlling it through methods.

Python provides three types of variables.

---

## Public Variable

Accessible from anywhere.

```python
self.name = "Suryansh"
```

---

## Protected Variable

Starts with a single underscore.

```python
self._country = "India"
```

It can still be accessed outside the class but should be treated as internal.

---

## Private Variable

Starts with double underscores.

```python
self.__salary = 50000
```

Private variables cannot be accessed directly outside the class.

---

# 7. Data Extraction

Pandas can be used to read different file formats.

Import pandas

```python
import pandas as pd
```

---

## Read CSV

```python
pd.read_csv(file_path)
```

Using a separator

```python
pd.read_csv(file_path, sep=",")
```

---

## Read JSON

```python
pd.read_json(file_path)
```

---

## Read Parquet

```python
pd.read_parquet(file_path)
```

---

## head()

Displays the first five rows.

```python
df.head()
```

---

# 8. Class Methods

A class method works with the class instead of an object.

Use the `@classmethod` decorator.

```python
@classmethod
def change(cls, company):
    cls.company = company
```

---

## cls

`cls` refers to the class.

It is similar to `self`, but

- `self` → Current Object
- `cls` → Current Class

---

## Calling a Class Method

Using an object

```python
obj.change("Google")
```

Using the class name (Recommended)

```python
Employee.change("Google")
```

---

# Difference Between self and cls

| self | cls |
|------|-----|
| Refers to the current object | Refers to the class |
| Used in instance methods | Used in class methods |
| Can access instance variables | Used to access or modify class variables |

---

# Difference Between Class Variables and Instance Variables

| Class Variable | Instance Variable |
|---------------|-------------------|
| Shared by all objects | Unique to every object |
| Declared inside the class | Declared inside the constructor |
| Accessed using class name or self | Accessed using self |

---

# Key Points

- A class is a blueprint for creating objects.
- An object is an instance of a class.
- Constructors initialize object data.
- Class variables are shared among all objects.
- Instance variables belong to individual objects.
- Methods define the behavior of a class.
- Encapsulation helps protect object data.
- Public, protected, and private variables provide different levels of access.
- Pandas can read CSV, JSON, and Parquet files.
- `@classmethod` is used to modify or access class variables.
- `self` refers to the current object, while `cls` refers to the class.