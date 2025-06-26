class Vector:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y)
  
  def __sub__(self, other):
    return Vector(self.x - other.x, self.y - self.y)
  
  def __mul__(self, other):
    return Vector(self.x * other.x, self.y * other.y)
  
  def __str__(self):
    return f"Vector({self.x}, {self.y})"
  
v1 = Vector(2, 3)
v2 = Vector(4, 6)

v3 = v1 + v2 # Calls __add__
print(v3)

v4 = v3 - v1 # Calls __sub__
print(v4)

v5 = v1 * 5


