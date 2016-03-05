# .keys(), .values(), .items() methods

# iterating over the dictionary is iteration over its keys
d1 = {'uno': 'one', 'dos': 'two', 'tres': 'three'}

# iteration over the keys
for key in d1:
	print(key)

# more obvious iteration over the keys
for key in d1.keys():
	print(key)

# If we want to iterate over the values
for value in d1.values():
	print(value)

# If we want to iterate over key value pairs
# using this kind of syntax we will get tuples
for item in d1.items():
	print(item)

# iterkeys, itervalues, iteritems in Python 2
# viewkeys, viewvalues, viewitems in Python 2

# .keys() returning a special data type
print(d1.keys()) # dict_keys(['uno', 'dos', 'tres'])

# So we take this value and assign it to something
keys = d1.keys() # keys will reflect the mutation of a dictionary
print(keys)

# Adding new key value pair
d1['cinco'] = 'five'
print(d1)

# And view the keys
print(keys)

'''
for key in d1:
	if key == 'uno':
		del d1[key]
'''

# And when we will do that, we will get a runtime error
# We can not change the dictionary while we iterating over it
# This is just a consiquence how dictionary type is implemented
# in Python.

# If want to delete an element, we should identify an element
# and then delete them. Instead of deleting them in this for
# loop we instead create a SET of deleted keys and add the key
# that we want to delete to that set. And then we will create
# another for loop that iterates over the keys in deleted_keys
# and deletes them.

deleted_keys = set()

for key in d1:
	if key == 'uno':
		deleted_keys.add(key)

for key in deleted_keys:
	del d[key]
