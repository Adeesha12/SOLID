# SOLID

<details><summary> 

### Basic OOP Concepts 
</summary>

<details><summary> 


### **Class and Object**
 </summary>

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

<details><summary> 

### **Python Inheritance**
 </summary>


to have inheretance there should be a relationship within base class and child classes<br>
ex:-<br>
animal is base class to dog,cat and fish these child classes<br> 
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
super() method will get the super class / base class method  to child class.

if there same method in child class we can either call super class method or override the method.

uses of inheritance 
> 1.) since child class can inherete all the functionaly from parent class it allows code reusability <br>
> 2.) once functionality developed we can simply inherete it no need to reinvete the wheel, this way code become much cleaner <br>
> 3.) since we can inherete useful functionality to child class need to write other requireds funcitonaliy to the child class <br>
</details>

<details><summary>

### **Python Polymorphism**
 </summary>

the word polymorphism meaning is many-forms it means that every functions or classes either it built into user define it should be handle many senarios, 

>built in
```python
#// here we looks into len() built-in function
print(len('string'))           
print(len(['l','i','s','t']))
# // len function can handle string, list, tuples and many more data types 
```
>output
```
6
4
```
#### user define
```python
def add(x,y,z=0,a=0):
    return x+y+z+a

print(add(1,2))
print(add(1,2,5))
#// define function can handle more inputs
```
>output
```
3
8
```
#### classes
```python
class SriLanka():
	def capital(self):
		print("Colombo is the capital of Sri Lanka.")

	def language(self):
		print("Sinhala is the most widely spoken language of Sri Lanka.")

	def status(self):
		print("Sri Lanka is a developing country.")

class USA():
	def capital(self):
		print("Washington, D.C. is the capital of USA.")

	def language(self):
		print("English is the primary language of USA.")

	def status(self):
		print("USA is a developed country.")

def func(obj):    #// this is a example for duck typing in polymorsim 
	obj.capital()
	obj.language()
	obj.status()

obj_sri = SriLanka()
obj_usa = USA()

func(obj_sri)
func(obj_usa)

```
>output
```
Colombo is the capital of Sri Lanka.
Sinhala is the most widely spoken language of Sri Lanka.
Sri Lanka is a developing country.
Washington, D.C. is the capital of USA.
English is the primary language of USA.
USA is a developed country.
```

<details><summary> 

###  ways of implementing polymorphism in python 
</summary>

#### Duck typing

```python
class person01:
    def code(self,idea):
        idea.execute()
        
class person02:
    def execute(self): 
        print("Practice make everything perfect")

idea = person02() #// create person02 object

quote = person01()#// person01 object

quote.code(idea)#// calling the function by giving idea as the argument.
```
>output
```
Practice make everything perfect
```
Duck typing is a concept that says that "type" of the object is a matter of concern only at runtime.
the idea is that you don't need a type in order to invoke an existing method on an object if a method is defined on it, it can invoke.

#### Operator overloading

```python
class Vehical:
    def __init__(self,fare):
        self.fare = fare
    #// operator + overloading 
    def __add__(self,other):   
        return self.fare + other.fare
    #// operator < overloading
    def __lt__(self,other):
        return self.fare < other.fare
        
bus = Vehical(50)
car = Vehical(30)

total_fare = bus + car #// objects with operators 
is_gerater = bus < car #// objects with operators 

print(total_fare)
print(is_gerater)
```
>output
```
80
False
```
if we does not operator overloading + ,< or any other operator in user-define class it does not work instead return TypeError 

#### Method Overloading

```python
class Cal:
    def total(self,a=0,b=0,c=0): #// this is method overloading 
        return int(a+b+c)
    
    
c = Cal()
print(c.total())
print(c.total(1))
print(c.total(1,2))
print(c.total(1,2,3))
```
>output
```
0
1
3
6
```
#### Method overiding

```python
class HardWork:
    def __init__(self) -> None:
        self.value = "hard work beats talent"
        
    def practice(self):
        print(self.value)
        
    def consistency(self): #// this method override by child class "consistency" method
        print('Never stop working hard')
        
class Programming(HardWork):
    
    def consistency(self):#// this method overriding the base class "consistency" method
        print('never stop working hard for your dreams...!')
    
python = Programming()

python.practice()
python.consistency()
```
>output
```
hard work beats talent
never stop working hard for your dreams...!
```
method overriding help us to access and change the parent class logics whatever we need.

</details>
</details>

<details><summary>

### **Python Abstraction** </summary>
 
Abstraction in python means that hiding data/class form user to reduce the complexcity of software.
```python
from abc import ABC,abstractmethod

class Vehical(ABC):
    @abstractmethod
    def mileage(self):
        pass
    
class Car(Vehical):
    
    def mileage(self):
        print('25km per liter') 
        
class Van(Vehical):
    
    def mileage(self):
        print('15KM per liter')
        
class Plane(Vehical):
    
    def mileage(self):
        print('1km per liter')
        
car = Car()
print(car.mileage())
```
>output
```
25km per liter
None
```
1.in python , abstract class hold both abstract methods and normal methods <br>
2.derive class definition define on abstract base class  <br>
3.there is no initiate in abstract class, in abstract class cannot create object <br>
4.there is no way to define interface on python,instead we can use keyword abstract class itself <br>
</details>
<details><summary>

### **Python Encapsulation** </summary>


</details>


Coupling
Cohesion
Association
Aggregation
Composition
</details>


