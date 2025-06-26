class Employee:
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary

  @property
  def first_name(self):
    l = self.name.split(" ")
    return l[0]
  
  @first_name.setter # Where first_name nee to same as where we declare @property decorater..
  def first_name(self, first):
    l = self.name.split(" ")
    new_name = f"{first} {l[1]}"
    self.name = new_name

e = Employee("Jack Doe", 41000)

print(e.first_name) # e.first_name is a function we are using it like variable/operater because of @property decorater...
e.first_name = "John" # Here we are calling last function becuse we add "John" so it use last function and update the name and then split it...
print(e.name)