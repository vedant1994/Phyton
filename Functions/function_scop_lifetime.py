def sum(a, b):
  # a and b are local variable we can't access it anywhere.
  c = a+b
  return c

def greet():
  z =32 # local variable we can't access it outside this function.
  
  print("Hello, World!")

z = 8 # z is gloable variable we can access it from anywhere.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print(sum(a, b))
