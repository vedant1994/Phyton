print("Break Statement")
for i in range(0,60):
  print(i)
  if i == 11:
      break # Cancle the exicution of this loop now

print("\n")
print("Continue Statement")
for i in range(0,60):
  if i == 11:
      continue # Skip the 11.
  print(i)

print("\n")
print("Pass Statement")
for i in range(0,60):
  print(i)
  if i == 11:
      pass # Loop will continue as it is.... 