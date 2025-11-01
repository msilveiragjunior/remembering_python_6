# --- Dictionaries --- #
# Dictionaries are a pair of key-value defined by the
# curly braces({}) symbol
alien_0 = {'color': 'green', 'points': 5}
# We can access the value of a dictionary by using it's key
print(alien_0['color'])
# We can add new values to dictionaries dinamically
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# This will show all the values of the dictionary
# We can modify the value of a key by simply redefining it
alien_0['y_position'] = 35
print(alien_0)
# we can delete information from a dictionary by using the
# instruction del
del alien_0['points']

# --- method .items() --- #
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}
for k, v in user_0.items():
    print(k + "\n")
    print(v + "\n")
# We can use .items() to return the key and the value in a
# given dictionary

# --- putting the key names inside a list variable --- #
list_01 = []
for user in user_0.keys():
    list_01.append(user)
print(list_01)
# by using the .keys() method we managed to take the keys
# informations and append to a list
# the .values() method will return the values of a given
# dictionary

# --- What is a (set) --- #
# A set is like a list, but it can only contain one value
# of each information, for example a set of {0,1,0,1} would
# contain only the numbers 0 and 1 if printed
user_0['rename'] = 'fermi'
print(set(sorted(user_0.values(), reverse=True)))

# --- Nesting dictionaries inside a list --- #
aliens = []
for alien in range(30):
    aliens_new = {'speed': 'slow', 'points': '5', 'color': 'green'}
    aliens.append(aliens_new)
for alien in aliens[:10]:
    print(alien)
# This will create 30 aliens dictionaries and append it to a list
# The print will show only the first 10
print(str(len(aliens)))
# This print will show the lenght of the list
# Lets modify the first 5 aliens
for alien in aliens[0:15]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow',
        alien['speed'] = 'medium',
        alien['points'] = '10'
for alien in aliens[:5]:
    print(alien)
# This will change the type of the first 15 aliens to yellow
for alien in aliens[:5]:
    if alien['color'] == 'yellow':
        alien['color'] = 'red',
        alien['speed'] = 'fast',
        alien['points'] = '15'
# This will change the type of the first 5 aliens to red

# --- Nesting a list inside a dictionary --- #
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
print(pizza['toppings'])
# This is an example of how to nest a list inside a dictionary
