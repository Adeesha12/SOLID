class Vehical:
    def __init__(self,fare):
        self.fare = fare
    
    def __add__(self,other):
        return self.fare + other.fare
    
    def __lt__(self,other):
        return self.fare < other.fare
        
bus = Vehical(50)
car = Vehical(30)

total_fare = bus + car
is_gerater = bus < car 

print(total_fare)
print(is_gerater)