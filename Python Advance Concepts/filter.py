def is_greater_than_9(x):
  if x>9:
    return True
  else:
    return False
  
a = [1, 3, 6, 7, 9, 8, 255, 587, 44]

new = list(filter(is_greater_than_9, a))
print(new)