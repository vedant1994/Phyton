# Class: Class is a nothing a blueprint or template. Eg. Form for an Exam that contains name, age, electives, father's name etc...

# Objects: Specific instance created from the template (Class). Eg. form which contains the data for John Doe

class Employee:
  company = "Google"

  def get_salary(self): # self is imported here because self is a way to reference the object of the class which is being created
    print(self)
    return 50000
  
# e and e2 is self as a object....

e1 = Employee() # An object of class employee is created here
print((e1.get_salary())) # Employee get salary method is called

e2 = Employee() 
print(e2.get_salary())
print(e2.company)