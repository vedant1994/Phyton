def sum(a, b):
  # a and b are local variable we can't access it anywhere.
  c = a+b
  return c

z = 8 # z is gloable variable we can access it from anywhere.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print(sum(a, b))
