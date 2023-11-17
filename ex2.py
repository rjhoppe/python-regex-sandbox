import re

'''
Requirements:
# identify any references to occupations in a comment
# EX: Doctor Smith, Officer Jimmy, Private Sally
'''

# pattern = re.compile("^[A-Z]{1}+[a-z]+\s[A-Z]{1}$+[a-z]$")
# pattern = re.compile("^[A-Z]{1}+[a-z\s]$")

# pattern = re.compile("[A-Z]{1}+[a-zA-Z]+\s+[A-Z]{1}+[a-z]{1}+[a-zA-Z]+")

pattern = re.compile("[A-Z]{1}+[a-zA-Z]+\s+[A-Z]{1}+[a-z]{1}+[a-zA-Z]+")

match = pattern.search("The HCSO is doing a great job.")
if match != None:
  print(match)
  print('Regex works!')
else:
  print('Regex failed')

# print(pattern.search("Doctor Smith"))
# print(pattern.search("Officer Jimmy was so very helpful"))
# print(pattern.search("I don't know why someone likes this Officer."))
# print(pattern.search("I've worked with the military for a long time and Private Sally is the worst"))