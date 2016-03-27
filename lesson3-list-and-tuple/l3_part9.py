# Unpacking
# ==================================================

# multiple assignments in one line
x, y = 1, 2
print(x)
print(y)

# performing swaps
x, y = y, x
print(x)
print(y)

# ==================================================
# With agregate types like lists and tuples we can unpack
# those types.
from datetime import date
profile = 'John', 'Quincy', 'Adams', date(1767, 7, 11)

first_name, middle_name, last_name, birthday = profile
print(birthday)

# ==================================================
# We will get an error if the number of itmes inside the tuple
# will not be equal to the number of variables.
profile1 = 'John', 'Adams', date(1767, 7, 11)

# first_name, middle_name, last_name, birthday = profile1
# print(birthday)

# ==================================================
fruits = ['apple', 'banana', 'apple', 'pear', 'strawberry']
fruit1, fruit2, fruit3, fruit4, fruit5 = fruits
print(fruit1)

# ==================================================
fruits1 = ['apple', 'banana', 'apple', 'pear', 'strawberry']
first_fruit, *remaining_fruits = fruits1
print(first_fruit)
print(remaining_fruits)

# ==================================================
fruits2 = ['apple', 'banana', 'apple', 'pear', 'strawberry']
first_fruit1, second_fruit1, *remaining_fruits1 = fruits2
print(first_fruit1)
print(second_fruit1)
print(remaining_fruits1)
