# Decorator is a function that takes a function, it creates a new function inside its body (wrapper). Then it  return that new function

def decorator(func): # Where func = Function which one we need to call like here while calling decorator we take say_hello() function

  def wrapper():
    print("I am about to execute a hello...")
    func() # Print say_hello() function...
    print("I have executed this function")
  return wrapper

'''
We have two methods for decorater..
   1)
  @decorator
  def say_hello():
      print("Hello!")

  2)
  # f = decorator(say_hello)
  # f()
  Don't need to call say_hello() function....
'''

@decorator
def say_hello():
  print("Hello!!!")

say_hello()