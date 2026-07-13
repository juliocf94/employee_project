class Employee:
    def __init__(self, id_employee, name, salary):
        self.id_employee = id_employee
        self.name = name
        self.salary = salary
        
    def annual_salary(self): 
        return self.salary * 12
    
    def is_high_salary(self):
        return self.salary >= 1000