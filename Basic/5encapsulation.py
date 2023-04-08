class Employee:
    def __init__(self,name,project) -> None:
        self.name = name
        self.project = project
        
    def work(self):
        print(f'{self.name} is working on {self.project}')

Emp1 = Employee('Adeesha','Crow')
Emp1.work()

    