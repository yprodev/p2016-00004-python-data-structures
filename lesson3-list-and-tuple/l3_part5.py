# Set item
# ==================================================
fruits = ['apple', 'banana', 'apple', 'pear', 'strawberry']

fruits[3] = 'watermelon'
print(fruits)

fruits[3:5] = 'orange', 'orange'
print(fruits)

# ==================================================
from datetime import date
profile = 'John', 'Adams', date(1735, 10, 30)

profile[1] = 'Tyler' # We will get an error because of tuple is immutable
print(profile)

profile[1:3] = 'Tyler', date(1970, 3, 29) # We will get an error because of tuple is immutable
