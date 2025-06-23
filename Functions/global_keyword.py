def sum(a, b):
  print("Hey i am summing.")
  c = a + b
  global z  # Declare z as a global variable to modify it
  z = 10  # Modify the global variable z
  return c

z = 5
print(sum(10, 20))
print(z)