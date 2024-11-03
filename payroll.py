#Base class
class Employee:
    def __init__(self,emp_id,emp_name):
        self.emp_id=emp_id
        self.emp_name=emp_name

        def calculate_payroll(self):
         raise NotImplementedError("subclasses must implement calculate_payroll method")

#inherits from Employee
    class salaryEmployee(Employee):
        def __init__(self, emp_id, emp_name,weekly_salary):
            super().__init__(emp_id, emp_name)
            self.weekly_salary = weekly_salary

        def calculate_payroll(self):
            return self.weekly_salary

#inherits from Employee      
class HourlyEmployee(Employee):
    def __init__(self,emp_id,emp_name,hours_worked,hourly_rate):
      super().__init__(emp_id, emp_name)
      self.hours_worked = hours_worked
      self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate

#inherits from salaryEmployee
class CommisssionEmployee(salaryEmployee):
    def __init__(self, emp_id, emp_name,commision,weekly_salary):
        super().__init__(emp_id, emp_name)
        self.commision=commision
    
    def calculate_payroll(self):
        return super().calculate_payroll() + self.commision
    
    #For example
    employees=[
       salaryEmployee(emp_id=3,emp_name="Cynthia",weekly_salary=5000),
       HourlyEmployee(emp_id=5,emp_name="Tabbs",hours_worked=30,hourly_rate=15),
       CommisssionEmployee(emp_id=7,emp_name="Stacy",weekly_salary=6000,commission=200)
    ]
for employee in employees:
   print(f"{employee.name}'s payroll: {employee.calculate_payroll()}")
    