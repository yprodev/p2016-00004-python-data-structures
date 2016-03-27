# Methods specific to lists
# ==================================================
# Adding new item
fruits = ['apple', 'banana', 'apple', 'pear', 'strawberry']
fruits.append('watermelon')
print(fruits)

# Adding new sublist
fruits.append(['dragonfruit'])
print(fruits)

# Clear all the items from the list
fruits1 = ['apple', 'banana', 'apple', 'pear', 'strawberry']
fruits1.clear()
print(fruits1)

# The same as..
fruits1 = ['apple', 'banana', 'apple', 'pear', 'strawberry']
print(fruits1)
del fruits1[:]
print(fruits1)

print('=========================================================')

fruits2 = ['apple', 'banana', 'apple', 'pear', 'strawberry']
fruits2.extend(['watermelon', 'watermelon', 'dragonfruit'])
print(fruits2)

# We could also extend with tuple
fruits2 = ['apple', 'banana', 'apple', 'pear', 'strawberry']
fruits2.extend(('watermelon', 'watermelon', 'dragonfruit'))
print(fruits2)

# We could also extend with set
fruits2 = ['apple', 'banana', 'apple', 'pear', 'strawberry']
fruits2.extend({'watermelon', 'watermelon', 'dragonfruit'})
print(fruits2)

print('=========================================================')

# The insert method takes an index and item and puts it in the 
# position within a list we want to place at.
fruits3 = ['apple', 'banana', 'apple', 'pear', 'strawberry']
fruits3.insert(3, 'dragonfruit')
print(fruits3)

fruits4 = ['apple', 'banana', 'apple', 'pear', 'strawberry']
fruits4.pop()
print(fruits4)

print('=========================================================')

# list as a stack
fruits5 = []
for fruit in ('apple', 'banana', 'pear', 'strawberry'):
	print("Appending:", fruit)
	fruits5.append(fruit)

print(fruits5)

while fruits5:
	print("Poping: ", fruits5.pop())

print('=========================================================')

fruits6 = ['apple', 'banana', 'apple', 'pear', 'strawberry']
fruits6.remove('pear')
print(fruits6)
# If we try to remove pear once more, we will get an error

# Now we will remove the first instance with two similar
fruits6 = ['apple', 'banana', 'apple', 'pear', 'strawberry']
fruits6.remove('apple')
print(fruits6)

print('=========================================================')

fruits7 = ['apple', 'banana', 'apple', 'pear', 'strawberry']
fruits7.reverse()
print(fruits7)

# We can sort items by the key
# like length (key=len)
# like reverse order (reverse=True)
fruits8 = ['apple', 'banana', 'apple', 'pear', 'strawberry']
fruits8.sort()
print(fruits8)

print('=========================================================')
print('------------------------- TUPLES ------------------------')
print('=========================================================')

profile = 'John', 'Quincy', 'Adams'
print(sorted(profile))

# Tuple does not support reverse of sort methods
# because of immutable type
profile = 'John', 'Quincy', 'Adams'
print(list(reversed(profile)))





