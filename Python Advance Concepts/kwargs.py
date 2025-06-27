def marks(**kwargs):
  # Kwargs is a dictionary with all the key value pairs which were passed to marks
  for item in kwargs.keys():
    print(f"The marks of {item} are {kwargs[item]}.")

marks(shubham=34, vikram=54, jack=73, marie=90)