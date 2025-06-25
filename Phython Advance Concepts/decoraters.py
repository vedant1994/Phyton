# Decorator is a function that takes a function, it creates a new function inside its body (wrapper). Then it  return that new function

def decorator(func):
  def wrapper():
    print("I am about to execute a hello...")
    func()
    print("I have executed this function")
  return wrapper

def say_hello():
  print("Hello!")

# say_hello()

f = decorator(say_hello)
f()