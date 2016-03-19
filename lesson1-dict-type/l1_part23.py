# Attribute Dictionary

# Those how know JavaScript will find out what is the
# difference between object and dictionary.

# ==================================================
class attrdict(dict):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.__dict__ = self

# Creating the instance of the class above
quux = attrdict()

# Let's assign a value to this dictionary using the
# item syntax.
quux['x'] = 100

# Let's achieve it using the attribute syntax.
print(quux.x)

# Let's change it using the attribute syntax.
quux.x = 200

# Let's retriev it using the item syntax.
print(quux['x'])

# ==================================================
# We used two different methods on the same instance. But
# there is a problem. We want to be warned about the next
# code. On operationg systems like Linux this will go
# normally. But on Windows sometimes this code has the
# potential to lock up your computer.

from itertools import count
'''
try:
	for num in count(1):
		attrdict({i:i for i in range(1024*1024)})
except MemoryError:
	print('Out of memory after creating {} attrdicts'.format(num))

'''

# ==================================================
# We call a collect function from gc module in order
# to perform a gurbage collection.
'''
from gc import collect; collect()

'''

# ==================================================
# Let's take a look at better formulation of this.
# We are just assigning item syntax to a attribute
# syntax. They are using the same arguments (self,
# key). This will accomplish the same thing without
# the memory cycle.

class attrdict1(dict):
	__getattr__ = dict.__getitem__
	__setattr__ = dict.__setitem__
	__delattr__ = dict.__delitem__


# Let's evaluate this code.
try:
	for num in range(1,150+1):
		attrdict1({1:1 for i in range(1024*1024)})
except MemoryError:
	print('Out of memory after creating {} attrdicts'.format(num))

print('Survived creating {} attrdicts'.format(num+1))