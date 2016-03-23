# getitem syntax
# ==================================================

fruits = ['apple', 'banana', 'apple', 'pear', 'strawberry']

# retrive by indexing
print(fruits[0])

# slice notation
print(fruits[2:4]) # ['apple', 'pear']
print(fruits[:4]) # we are starting from the beggining of the list not including the item under the index of 4
print(fruits[2:]) # we are starting from the item under the index of 2 and moving to the end

# stepping
print(fruits[1::2]) # we are starting from the item under the index of 1 and stepping every 2 elements

# ==================================================
# The same syntax available for the tuple type
from datetime import date

profile = 'John', 'Quincy', 'Adams', date(1797, 7, 11)
print(profile[0])

# The slicing behaviour is identical
print(profile[2:4])

print(profile[::-1]) # We step through all the items in the list but in the REVERSE order
