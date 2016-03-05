# dict.clear() method

# 1. We are creating a dictionary with one key value pair
xs = {'one': 'uno'}
print(xs)

# 2. We are adding another key value pair
xs['two'] = 'dos'
print(xs)

# 3. And let's call clear on it
# This method only removes all the enties from the dictionary
xs.clear()
print(xs)

# If we create a dictionary and call id() on it
xs1 = {}
print(id(xs1)) # Unique ID number that is correspond with the memory location

# If we are going to clear this dictionary by reassigning this dictionary then
# we will see that the id() value will change. The existing dictionary can still
# be around in memory if something else is referensing it. But if we call the
# .clear() method we will not destroy the existing dictionary but we will
# destroy all of the entries.

# We will create a new dictionary
xs2 = {'one': 'uno'}
# We create a refference
ys1 = xs2
# We reassign a dictionary
xs2 = {}
# But the refference has not changed
print('The refference is unchanged', ys1)

### BUT If we will use .clear() method the refference will also change
xs3 = {'one': 'uno'}
ys2 = xs3
xs3.clear()
print('Clear method', ys2)
