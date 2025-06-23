# Two types of module in python:
#  1) Bulit in module ex: math module,
#  2) External module Which one made by us.

import math
import mymodule # This is External module which one made by us and we can import it easliy useing it's name and while calling "File name" . function which we want to call.
import requests


print(math.sqrt(100))

mymodule.hello()

r = requests.get("https://www.google.com")
print(r)