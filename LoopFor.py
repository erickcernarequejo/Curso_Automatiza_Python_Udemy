countries = ['Peru', 'Brazil', 'Chile', 'Bolivia']

for country in countries:
    print(country)

for country in countries:
    if country == "Peru":
        print(country)

for number, country in enumerate(countries):
    print(number)
    print(country)

my_data = {'name': 'Erick', 'age': 31}
for key, value in my_data.items():
    print(key)
    print(value)
