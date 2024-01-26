import re

texto = '''Hello World.
I like Python!!!!!
My first number is 987-654-321
'''

# search first digit
print(re.search(r'\d', texto))

# search all elements
print(re.findall(r'\d', texto))

print(re.search(r'^hello', texto, flags=re.I))

# Search point
print(re.findall(r'[^\w\s]', texto))

# Validate date
dates = '''
13-04-2021
2021-13-04
2021-04-13
'''

print(re.findall(r'\d{2}-\d{2}-\d{4}', dates))

# Validate User 4 - 14 only numbers and letters
text = '''
usuario10
abc
10
'''
print(re.findall(r'[a-z0-9]{4,14}', text))