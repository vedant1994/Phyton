# Write to a file called John Doe.txt. It should contain data about John Doe.

f = open("John Doe.txt", "w")

string = '''
John doe ia a nice guy and he lives in NY.
'''

f.write(string)
f.close()