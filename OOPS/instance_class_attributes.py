class Employee:
  company = "Google" # This is class variable..

  def __init__(self, salary, name, bond, company):
    self.salary = salary # Create an instance attribute of name salary and assign it with salary
    self.name = name
    self.bond = bond
    self.company = company #Instance variable

  def get_salary(self):
    return self.salary

  def get_info(self):
    print(f"The name of the employee is {self.name}. salary is {self.salary}. The bond is {self.bond} year.")


e1 = Employee(51000, "John Doe", 4, "Tesla")
print(e1.company) # Will always print instance attribute whenever present
print(Employee.company) # This will always print class attribute