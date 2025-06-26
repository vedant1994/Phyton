class Employee:
  company = "HP"
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary

  # Instance Method(Default)
  def print_info(self):
    print(f"The name of the employee is {self.name} and the salary is {self.salary}")

  # Static Method
  @staticmethod
  def sum(a,b):
    return a+b
  
  # Class Method
  @classmethod 
  def print_company(cls):
    print(cls.company)

  @classmethod
  def change_company(cls, new_company):
    cls.company = new_company



e1 = Employee("Jack", 40000)
e2 = Employee("Oggy", 49000)

# e1.print_info()
# e2.print_info()
# print(e2.sum(5,20))

e1.print_company()
e1.change_company("DELL")
e1.print_company()

print(Employee.company)