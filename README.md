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
</details>


