class Employee:

  def __init__(self, salary, name, bond):
    self.salary = salary # Create an instance attribute of name salary and assign it with salary
    self.name = name
    self.bond = bond

  def get_salary(self):
    return self.salary

  def get_info(self):
    print(f"The name of the employee is {self.name}. salary is {self.salary}. The bond is {self.bond} year.")
  
e1 = Employee(34000, "John Doe", 4)
print(e1.get_info())
