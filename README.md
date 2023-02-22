# SOLID
## oop learning
## Basic
<details><summary> <a color = 'green'>details</a> </summary>

### **Class**
```python
class Employee: #// this is a class
    pass
```

### **Class attribute**
```python
class Employee: #// this is a class
    company_name = 'BST' #// this is class attribute

emp1 = Employee()   #// this is an object
emp2 = Employee()   #// this is an object

print(emp1.company_name)
print(emp2.company_name)
```
> output
```
  'BST'
  'BST'
```

### **Instance attribute**
```python
class Employee: #// this is a class
    company_name = 'BST' #// this is class attribute

emp1 = Employee()   #// this is an object
emp2 = Employee()   #// this is an object

emp1.name = 'rick'  #// this is a instance attribute

print(emp1.company_name)
print(emp2.company_name)
   
print(emp1.name)   
print(emp2.name) 
```
There is a one instace attribute so it will throw an attribute for emp2.name which is not exist !
> output
```
BST
BST
rick
Traceback (most recent call last):
  File "/_path_/SOLID/file_name.py", line 13, in <module>
    print(emp2.name)   
AttributeError: 'Employee' object has no attribute 'name'
```
Pythonic way of declaring attribute 

```python
class Employee: #// this is a class
    pass

emp1 = Employee()   #// this is an object
emp2 = Employee()   #// this is an object

Employee.company_name = 'BST' #// this is class attribute

emp1.name = 'Rick'       #// this is an instance attribute
emp1.lastname ='Bernard' #// this is an instance attribute
emp2.name = 'Morty'      #// this is an instance attribute
emp2.lastname = 'Meyer'  #// this is an instance attribute

print(emp1.company_name)
print(emp2.company_name)
   
print(emp1.name +' '+emp1.lastname)   
print(emp2.name +' '+emp2.lastname)   
```
```
BST
BST
Rick Bernard
Morty Meyer
```
**But this kind of declaration are not practical to use because it violate DRY (don't repeat youself) method
and create much complexity.**

* class varibles preferes to declare before the all methods

* for instace attribute it is recommand to use __init__ method in a class,when every time creating an instaces 
it variables are automatically assigned

```python
class Employee:               #// this is a class
    company_name = 'BST'      #// this is class attribute
    
    def __init__(self,name,lastname) -> None:
        self.name = name              #// this is an instance attribute
        self.lastname = lastname      #// this is an instance attribute
        
emp1 = Employee('Rick','Bernard')     #// this is an object with instance attributes
emp2 = Employee('Morty','Meyer')      #// this is an object with instance attributes


print(emp1.company_name)
print(emp2.company_name)
   
print(emp1.name +' '+emp1.lastname)   
print(emp2.name +' '+emp2.lastname)     
```
```
BST
BST
Rick Bernard
Morty Meyer
```

```python
class Employee:           #// this is a class
    company_name = 'BST'  #// this is class attribute
    
emp1 = Employee()         #// this is an object

print(emp1.__dict__)      #// this printout the instace attriute as a dictionary which is none this point
print(emp1.company_name)  #// this print out class attribute

emp1.company_name = 'new company' #// this ia an instance attribute

print(emp1.__dict__)      #// this printout the instace attriute as a dictionary
print(emp1.company_name)  #// this printout the instace attriute 

print(Employee.company_name) #// this print out class attribute
```
```
{}
BST
{'company_name': 'new company'}
new company
BST
```
### **Python Inheritance**

to have inheretance there should be a relationship within base class and child classes
ex:-
animal is basle class to dog,cat and fish these child classes 
vehical is base class to car,van and boat child classes 

```python
class Animal:                     #// this is the base class / super class
    
    def __init__(self,age,sex) -> None: #// instance attributes
        self.age = age
        self.sex = sex
        
    def activity(self):
        return f"i can walk and my age {self.age} and i am a {self.sex}"
    
    
class Dog(Animal):                 #// this is the inheretance 
    
    def activity(self):
        return super().activity()  #// this call the superclass/baseclass method 

class Fish(Animal):

    def __init__(self, age, sex) -> None: #// this call the super class init method
        super().__init__(age, sex)

    def activity(self):            #// this is method overriding
        return f"i can swim and my age {self.age} and i am a {self.sex}"

        
dog = Dog(15,'male')  #// this is object/instance to child class
fish = Fish(5,'female')  #// this is object/instance to child class

print(dog.activity())
print(fish.activity())
```
>output
```
"i can walk and my age 15 and i am a male"
"i can swim and my age 5 and i am a female"
```
super() method will get the super class / base class method  to child class

if there same method in child class we can either call super class method or override the method

uses of inheritance 
> 1.) since child class can inherete all the functionaly from parent class it allows code reusability
> 2.) once functionality developed we can simply inherete it no need to reinvete the wheel, this way code become much cleaner 
> 3.) since we can inherete useful functionality to child class need to write other requireds funcitonaliy to the child class

</details>


