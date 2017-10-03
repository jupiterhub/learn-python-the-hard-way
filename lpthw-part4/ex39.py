# Dictionary (dict)

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10) # print '-' 10x (=,, -, and / does NOT work)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10) # print '-' 10x
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# print every state abbreviation
print('-' * 10) # print '-' 10x
# key, value in list
print("states:", states)
print("states.items():", states.items())
print('list(states.items()):', list(states.items()))

# .items() - converts the key value pair to iterable pairs
# if you pass only 1 variable in the loop in for you will get the pair object
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
# also works without wrapping to list.
# cities.items vs list(cities.items()) same result
print('-' * 10) # print '-' 10x
for abbrev, city in cities.items():
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get abbreviation by state that might not be there

state = states.get('Texas')
# states['Texas'] - throws error. use get()
if not state:
    print("Sorry, no Texas")

# get a city with a default value
city = cities.get('TX', 'Does not exist')
print(f"The city for the state 'TX' is: {city}")
