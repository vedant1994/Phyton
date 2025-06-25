class Animal: # Parent class (superclass)
  location = "Canada"
  def __init__(self, name):
    self.name = name
  def speak(self):
    print("Generic animal sound")

class Dog(Animal): # This is how inheritance is done in Python
  def speak(self):
    super().speak() # With the use of SUPER we can call the parentclass or superclass function in subclass or child class. 
    print("woof!!")


# a = Animal("Dog")
# a.speak()

d =Dog("Brunoo")
print(d.location)
d.speak()
