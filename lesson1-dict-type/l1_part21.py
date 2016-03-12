# Dict versus Object

class Foo:
	pass

foo = Foo()
foo.x = 10
print(foo.x) # 10

# We could also explicitly use the get attribute protocol
print(getattr(foo, 'x')) # getattr protocol foo - object, 'x' - attribute

# ================================================================

# Let's look on equvivalent steps of a dictionary

bar = {}

bar['y'] = 15
print(bar['y']) # 15

# We could excplicitly invoke the getitem protocol by improting
# getitem from operator module
from operator import getitem

print(getitem(bar, 'y'))

# ================================================================

# This is a dictionary for a class. This contains all that state for that
# instance of that class. So in the case of the foo variable foo is an
# instance of a class Foo. In this case foo has some instance state that
# some state local only to the instance itself, not share with the class.
# And this state happens to be a attribute called x, whose value is set to
# 10.
print(foo.__dict__) # {'x': 10}


# ================================================================

class Base:
	z = 10

class Derived(Base):
	pass

d = Derived()

print(d.__dict__) # {} - empty

# It's empty because this instance has no something unique

d.x = 15
print(d.__dict__) # {'x': 15}

Base.xyz = 10
print(d.__dict__) # {'x': 15} -- in other word - nothing will change

# But we can get it through getattr protocol
print(getattr(d, 'z')) # 10

# ================================================================

# Benchmarking instance object and dictionary information retrival
class Foo2:
	x = 10

foo2 = Foo2()

bar2 = {'y': 20}

% timeit foo2.x
% timeit bar2['y']

# ================================================================

class Foo3:
	def __getitem__(self,key):
		if key == 'x':
			return 10
		raise KeyError('no such key {}'.format(key))

	def __getattr__(self,attr):
		if attr == 'x':
			return 100
		raise AttributeError('no such attr {}'.format(attr))

foo3 = Foo3()

% timeit foo3.x
% timeit foo3['x']

# ================================================================


# There are to different methods:
#			__getattr__
#			__getattribute__ 	<-- this is faster

class Foo4:
	def __getitem__(self, key):
		if key == 'x':
			return 10
		raise KeyError('no such key {}'.format(key))

	def __getattribute__(self, attr):
		if attr == 'x':
			return 100
		raise AttributeError('no such attr {}'.format(attr))



foo4 = Foo4()

% timeit foo4.x
% timeit foo4['x']










