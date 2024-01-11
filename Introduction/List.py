countries_america = ['Peru', 'Brazil', 'Chile', 'Bolivia']
print(countries_america[0])
print(countries_america[-1])

# Slicing name_list[start:stop]
print(countries_america[0:2])
print(countries_america[1:])
print(countries_america[:2])

# Methods and operations
countries_america.append('Colombia')
print(countries_america)

countries_america.insert(0, 'Argentina')
print(countries_america)

countries_europe = ['UK', 'Alemania', 'España']

countries = [countries_america, countries_europe]
print(countries)

countries_america.remove('Bolivia')
print(countries_america)

countries_america.pop(0)
print(countries_america)

del countries_america[0]
print(countries_america)

numbers = [4, 3, 10, 7, 1, 2]

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

numbers[0] = 1000
print(numbers)

countries_europe_copy = countries_europe.copy()
print(countries_europe_copy)




