# Addition and Multiplication
# ==================================================

print(['apple'] * 3) # ['apple', 'apple', 'apple']
print((123, 456) * 3) # (123, 456, 123, 456, 123, 456)

print([['apple']] * 3) # [[apple], [apple], [apple]]
print([['apple'], ['orange']] * 3) # [['apple'], ['orange'], ['apple'], ['orange'], ['apple'], ['orange']]


# ==================================================
# Addition
print(['apple'] + ['banana']) # ['apple', 'banana']

# ['apple'] + 'banana' # We will get a type error
# ['apple'] + list('banana') # banana will be separate letters

print(('John') + ('Tyler'))

# id (place in memory) will not change after adding new item
fruits = ['apple']
print(id(fruits))
fruits += ['banana']
print(id(fruits))

# In case of tuples this will differ
# the id will change after adding new item
profile = 'John',
print(id(profile))
profile += 'Tyler',
print(id(profile))
