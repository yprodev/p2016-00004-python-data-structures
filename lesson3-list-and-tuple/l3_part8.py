# iteration
# ==================================================

fruits = ['apple', 'banana', 'apple', 'pear', 'strawberry']

for fruit in fruits:
	print('My favourite fruit is the ', fruit)

for fruit in fruits[:3]:
	print('Favourite fruit is the ', fruit)

# We can delete the items as we iterate
for idx, fruit in enumerate(fruits):
	del fruits[idx]
	print('My favourite fruit is the ', fruit)
