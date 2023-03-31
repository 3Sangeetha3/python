class Employee:   
    def __init__(self, age = 0):   
         self._age = age   
      # using the getter method   
    def get_age(self):   
        return self._age   
      # using the setter method   
    def set_age(self, a):   
        self._age = a   
    
Emp = Employee()   
    
#using the setter function  
Emp.set_age(19)   
    
# using the getter function  
print(Emp.get_age())   
    
print(Emp._age)  