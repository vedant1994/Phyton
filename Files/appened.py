# Append to an existing file called John Doe.txt. It should contain data about John Doe.

f = open("John Doe.txt", "a")

string = '''
John doe initially lived in UK. He is a very nice guy
'''

f.write(string)
f.close()