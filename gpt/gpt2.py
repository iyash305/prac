class Employee:
        def __init__(self,name,salary):
            self.name = name
            self.salary = salary

        def get_info(self):
            return f"Name : {self.name}, Salary: {self.salary}"
        
class Manager(Employee):
        def __init__(self,name,salary,bonus):
            super().__init__(name,salary)
            self.bonus = bonus
        def get_total_salary(self):
            return self.salary + self.bonus
        def get_info(self):
            return super().get_info()

m1 = Manager("Yash", 5000,800)
print(m1.get_info())
print(m1.get_total_salary())
