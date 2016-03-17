# Semantics of Object versus Dictionaries


class Foo1:
	def __getattr__(self, attr):
		return attr
	def __getitem__(self, key):
		return key

foo1 = Foo1()


# ==================================================
# Using get item protocol to get three keys
print(foo1['two words'])
print(foo1['123'])
print(foo1['abc/def'])

# ==================================================
# Using get attr protocol to get three keys

# foo1.two words
# foo1.123
# foo1.abc/def

# will give us an error

# ==================================================

class Foo2:
	def __init__(self):
		self.x = 10

foo2 = Foo2()

print(foo2.x) # retrieving as an attribute
print(foo2.__dict__['x']) # retrieving as a dictionary key


# ==================================================

class Base:
	x = 10

class Derived(Base):
	pass

d = Derived()
print('We have to see base attribute', d.x) # Getting as an attribute

# We may say that it is not possible for dictionary.


# ==================================================

# After we add something to an instance we can get it through get_attr
# protocol.
Base.y = 100
print('Through get_attr protocol ', d.y)

# How we can do this with dictionary?
# We need to import ChainMap from collections module
from collections import ChainMap

b2 = {}
d2 = ChainMap({}, b2)

b2['x'] = 'hello'
print(d2['x'])

b2['x'] = 'bye'
print(d2['x'])

b2['y'] = 45
print(d2['y'])

d2['y'] = 50 # NOTE the property in the d2
print(d2['y'])

# ==================================================

class BaseA:
	x = 10

class BaseB:
	x = 100
	y = 200

class Derived(BaseA, BaseB):
	pass

d = Derived()
print(d.x) # x from BaseA
print(d.y) # y from BaseB

# How we could implement the same behaviour with dictionaries

ba = {'x': 10}
bb = {'x': 100, 'y': 200}

d3 = ChainMap({}, ba, bb)

print(d3['x']) # 10
print(d3['y']) # 200

# ==================================================

print(Derived.__mro__) # We will get a chain map of our classes

d4 = ChainMap({}, *(entry.__dict__ for entry in Derived.__mro__))
print(d4['x'], d4['y'])

# ==================================================

class Foo3:
	def __init__(self, x):
		self.x = x

foo3 = Foo3(10)
print(foo3.x)

# And now we wanna hide some behaviour, some computation
class Foo4:
	def __init__(self, x):
		self._x = x # NOTE: We are assigning value to the _x

	# ... and we create a property called x that hides
	# some computation
	@property
	def x(self):
		self._x += 1
		return self._x

foo4 = Foo4(350)
print(foo4.x) # 351
print(foo4.x) # 352
print(foo4.x) # 353


# How we could create the same behaviour with dictionaries?

class Foo5:
	def __init__(self, x):
		self._x = x

	def __getitem__(self, key):
		if key == 'x':
			self._x += 1
			return self._x
		raise KeyError('no such key {}'.format(key))

foo5 = Foo5(50)
print(foo5['x'])
print(foo5['x'])
print(foo5['x'])









































