class Animal:                     #// this is the base class / super class
    
    def __init__(self,age,sex) -> None: #// instance attributes
        self.age = age
        self.sex = sex
        
    def activity(self):
        return f"i can walk and my age {self.age} and i am a {self.sex}"
    
    
class Dog(Animal):                 #// this is the inheritance 
    
    def activity(self):
        return super().activity()  #// this call the superclass/baseclass method 

class Fish(Animal):
    
    def __init__(self, age, sex) -> None:
        super().__init__(age, sex)
    
    def activity(self):            #// this is method overriding
        return f"i can swim and my age {self.age} and i am a {self.sex}"

        
dog = Dog(15,'male')  #// this is object/instance to child class
fish = Fish(5,'female')  #// this is object/instance to child class

print(dog.activity())
print(fish.activity())
