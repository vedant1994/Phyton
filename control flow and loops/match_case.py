print("Enter value from below: \n 1) 122,12 2) 3, 3) 6")

a= int(input("Enter the number: "))

match a:
  case 1:
    print("The value is 122")
  case 2:
    print("The value is 3")
  case 3:
    print("The value is 6")
  case _:
    print("Better luck next time")