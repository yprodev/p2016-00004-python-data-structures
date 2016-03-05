# We can create dictionaries using literal syntax
xs = {1: 1, 2: 4, 3: 9}
print(xs)

# Another way we could create dictionary is to use Dict value constructor
# using a kye word argument. A key word argument represents a key and the
# value represents a value
xs1 = dict(one='uno', two='duo')
print(xs1)

# Another way to create a dictionary is to use a key value pairs
# Here we passing dictionary a list and the content of that list
# are tuples, where the first element represents a key and the
# second element represents a value. Please, note that values
# order will different every time.
xs2 = dict([
						('uno', 'one'),
						('duo', 'two'),
						('tres', 'three')
])
print(xs2)

# Another way to create a dictionary is dict.fromkeys() method
# It creates a dictionary using a collection as its' keys, setting
# the value of each key to None. This method was very useful
# before we had a set type. This is one way that people create
# set types using a dictionary type.
from string import ascii_lowercase
xs3 = dict.fromkeys(ascii_lowercase)
print('ascii_lowercase', xs3)


'''
# NOTE: That when we trying to constract a dictionary with a list
# type we'll get a type error.
'''
# xs4 = {[1,2,3]:10}

# Another way to create a dictionary is to use dict() and pass it
# an existing dictionary
xs5 = {1: 1, 2: 4, 3: 9}
ys1 = dict(xs5)
print(ys1)

# We should also cover very useful method - dict.update
# When you call dict.update on another dictionary you must pass it
# another mapping. Typically this means another dictionary. .update()
# will iterate through the keys of another dictionary and update the
# values of another dictionary with the values of those keys
xs6 = {1: 1, 2: 4, 3: 9}
ys2 = {}
ys2.update(xs6)
print(ys2)
