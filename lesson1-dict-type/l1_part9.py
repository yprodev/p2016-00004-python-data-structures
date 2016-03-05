# We can retrieve the element from a dictionary and remove it at the same time
# .pop() retrieves the element from a dictionary and removes that entry from a
# dictionary.

xs1 = {'one': 'uno', 'two': 'dos'}
print(xs1.pop('one')) # one
print(xs1) # {'two': 'dos'}

# If we try to execute .pop() method once more on the entry
# that does not exists in the dictionary we will get a traceback
# xs1.pop('one') 

# However .pop() method provides us ability to use default value
# like in .get() method. Is the key is no longer the part of the
# dictionary, we will see the default value.
print(xs1.pop('one', 'default'))


# If we would like to get and item inside of the dictionary that is
# the key value pair and also remove it from the dictionary we can
# use .popitem(). This will return the next item in the dictionary.
# Note, that the content of the dictionary is not sorted. .popitem()
# may retrieve any item of a dictionary. And you may not be able to
# predict what value it is.