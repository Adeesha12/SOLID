class Cal:
    def total(self,a=0,b=0,c=0): #// this is method overloading 
        return int(a+b+c)
    
    
c = Cal()
print(c.total())
print(c.total(1))
print(c.total(1,2))
print(c.total(1,2,3))