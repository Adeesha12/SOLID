class Vehicle:
    def __init__(self,fare):
        self.fare = fare
    
    def __add__(self,other):
        return self.fare + other.fare
    
    def __lt__(self,other):
        return self.fare < other.fare
        
bus = Vehicle(50)
car = Vehicle(30)

total_fare = bus + car
is_greater = bus < car 

print(total_fare)
print(is_greater)