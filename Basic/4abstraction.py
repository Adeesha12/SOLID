from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def mileage(self):
        pass
    
class Car(Vehicle):
    
    def mileage(self):
        print('25km per liter') 
        
class Van(Vehicle):
    
    def mileage(self):
        print('15KM per liter')
        
class Plane(Vehicle):
    
    def mileage(self):
        print('1km per liter')
        
car = Car()
print(car.mileage())