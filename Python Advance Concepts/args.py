def sum(*args):
  # Args will be a tuple of all the values passed to sum
  total = 0
  for item in args:
    total += item
  return total

print(sum(342, 8, 10))
