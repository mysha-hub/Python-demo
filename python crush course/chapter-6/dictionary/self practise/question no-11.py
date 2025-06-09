cities = {'new york': {'country':'america', 'population' : '8.5 million', 'fact': 'the city that never sleeps'},
          'paris': {'country':'france', 'population' : '2.1 million', 'fact': 'the city of lights'},
         'tokyo': {'country':'japan', 'population' : '14 million', 'fact': 'the city of the rising sun'},
         'london': {'country':'england', 'population' : '9 million', 'fact': 'the city of fog'},}
for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"\tCountry: {info['country'].title()}")
    print(f"\tPopulation: {info['population']}")
    print(f"\tFact: {info['fact'].title()}")
