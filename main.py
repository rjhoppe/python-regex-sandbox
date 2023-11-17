import re

# Example searching for all uppercase characters
# When you add ^ and $ the whole string has to match pattern
pattern = re.compile("^[A-Z]+$")
print(pattern.search("Hello World"))
print(pattern.search("HELLO WORLD"))
print(pattern.search("HELLOWORLD"))

# Example searching for all lowercase characters
pattern = re.compile("^[a-z]+$")
print(pattern.search("helloworld"))

# Match function looks for all matches
# Note: Removed ^ and $ which means the whole string doesn't
# have to match
pattern = re.compile("[a-z]+")
print(pattern.match("helloworld"))
print(pattern.match("hello world"))


# Allows lowercase or uppercase and allowing spaces
pattern = re.compile("^[a-zA-Z\s]+$")
print(pattern.match("Hello World"))
print(pattern.match("helloworld"))
print(pattern.match("hello world"))
print(pattern.match("hello wo8rld"))


