def repeat(n): # Repeat return decorator function...
  def decorator(func): # Decorator return wrapper function...
    def wrapper(a):
      for i in range(n):
        func(a)
    return wrapper
  return decorator

@repeat(7)
def say_hello(a):
  print(f"Hello! {a}")

say_hello("Vedant")