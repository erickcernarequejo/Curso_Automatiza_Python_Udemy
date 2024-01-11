dictionary = {'key1': 'value1',
              'key2': 'value2'}

my_data = {'name': 'Erick', 'age': 31}

print(my_data)
print(my_data['name'])

print(my_data.keys())
print(my_data.values())
print(my_data.items())

my_data['birth'] = 1892
print(my_data)

my_data.update({'birth': 1992, 'languages': ['English', 'Spanish']})
print(my_data)

my_data.pop('birth')
print(my_data)

del my_data['languages']
print(my_data)

my_data.clear()
print(my_data)
