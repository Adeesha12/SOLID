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
