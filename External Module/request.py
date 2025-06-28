import requests

r = requests.get('https://api.github.com/users/Vedant1994')

print(r.text)

with open("Vedant.txt", "w") as f:
  f.write(r.text)