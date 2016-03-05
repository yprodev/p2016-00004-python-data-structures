# .copy() method
# This method creates a copy of a dictionary
# This method will create a shallow copy
# What this means is the the values of the dictionary
# will not be copied. Only the keys will be copied. The
# values will be refferences to the values of the
# original dictionary.

xs1 = {'one': 'uno'}
ys1 = xs1.copy()
xs1.clear()
print(xs1) # {}
print(ys1) # {'one': 'uno'}

# Nested dictionary
xs2 = {'one': {'spanish': 'uno',
							 'german': 'ein',
							 'french': 'un'}}
print(xs2)

ys2 = xs2.copy() # Creating a copy of the nested dictionary
xs2['one'].clear() # Clearing the 'one' key in xs2 dictionary
# ys is a shallow copy
# This will make effect on xs2 and ys2 dictionaries
# Because the copy() that not make recursive copies of all of the substructures
# If we want a deep copy there is a module that provides a deep copy of a
# dictionary
print(ys2)