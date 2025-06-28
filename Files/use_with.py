with open("Files/vedant.txt", "r") as f:
  content = f.read()
  print(content) # No need to write f.close(). It will auto close the file.....
  