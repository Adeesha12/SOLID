class Employee:           #// this is a class
    company_name = 'BST'  #// this is class attribute
    
emp1 = Employee()         #// this is an object

print(Employee().company_name)
print(emp1.__dict__)      #// this printout the instance attribute as a dictionary which is none this point
print(emp1.company_name)  #// this print out class attribute

emp1.company_name = 'new company' #// this ia an instance attribute
Employee().company_name = 'bla'
print(emp1.__dict__)      #// this printout the instance attribute as a dictionary
print(emp1.company_name)  #// this printout the instance attribute 

print(Employee.company_name) #// this print out class attribute
print(Employee().company_name)