# delitem syntax
# ==================================================

fruits = ['apple', 'banana', 'apple', 'pear', 'strawberry']

del fruits[2]
print(fruits)

# We could also delete items using slice
fruits1 = ['apple', 'banana', 'apple', 'pear', 'strawberry']
del fruits1[1:3]
print(fruits1)

# ==================================================
from datetime import date
profile = 'John', 'Quincy', 'Adams', date(1767, 7, 11)

# del profile[1] # We will got an error
print(profile)
