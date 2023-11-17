import re

'''
Requirements:
# 3 lowercase letters
# 3-5 digits
# one symbol
# up to two uppercase characters (optional)
'''

# {} this means exactly
# EX: {3}[0-9] Exactly 3 numbers
pattern = re.compile("^[a-z]{3}[0-9]{3,5}[^a-zA-Z0-9]{1}[A-Z]{0,2}$")
print(pattern.search("ahd2331#AJ"))
print(pattern.search("lll44511.K"))
print(pattern.search("11144511."))
print(pattern.search("abc123456#JJ"))