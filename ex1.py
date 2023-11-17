import re

'''
Requirements:
# simple email format validator
# not robust enough for production - try a library
'''

# \ adding escapes
pattern = re.compile("^[a-zA-Z0-9\.\-_]+@{1}[a-zA-Z0-9]+\.{1}[a-zA-Z]{2,3}$")
print(pattern.search("rick@gmail.com"))
print(pattern.search("my_fancy.e-mail@fancyurl123.de"))
print(pattern.search("something.something.com"))
print(pattern.search("mail@something"))