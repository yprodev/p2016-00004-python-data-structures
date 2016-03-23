# Creating a tuple
# ==================================================

from datetime import date

profile = ('John', 'Quincy', 'Adams', date(1767, 7, 11))
print(profile)

# Creating with unnessesary parentacies
profile1 = 'John', 'Quincy', 'Adams', date(1767, 7, 11)
print(profile1)

# Lightweight syntax to create tuple with one item
profile2 = 'John',
print(profile2)

# Tuple function
profile3 = tuple(['John', 'Quincy', 'Adams', date(1767, 7, 11)])
print(profile3)

letters = tuple('apple')
print(letters) # ('a', 'p', 'p', 'l', 'e')

numbers = tuple(range(10))
print(numbers) # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Creating an empty tuple
profile4 = ()
profile5 = tuple()
print(profile4)
print(profile5)

print(type(profile4))