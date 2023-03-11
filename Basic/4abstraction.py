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