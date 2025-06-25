class Employee:
  company = "HP"
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary

  # Instance Method(Default)
  def print_info(self):
    print(f"The name of the employee is {self.name} and the salary is {self.salary}")

e1 = Employee("Jack", 40000)
e2 = Employee("Oggy", 49000)

e1.print_info()
e2.print_info()