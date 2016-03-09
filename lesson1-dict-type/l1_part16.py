# __getitem__ and __call__

# In Python we could talk how to interact with object as by
# using 'ad hock' protocols. Namely that object establishes
# that inherits to a protocol that it iherits to a protocol
# it says that it will responde to a particular message and
# a particular format. And there is assosiate semantics from
# other. One such protocol is __getitem__(). That means that
# object responds to a syntax of having a square bracket,
# after the name of the object and inside of square bracket
# is the key. In response of getting a key the object will
# return some value. That value in the case of dictionary
# may be some static value or in the case of dictionary
# subclass missing implemented could be some computation.

# Here is some simple example of this
d = {1: 1, 2: 4}
print(d[2])

# Invoking the protocol directly
print(d.__getitem__(2))

# The actual dict type of Python has a __getitem__
# __function__. But any arbitrary object in Python can also
# have one.

class Foo:
	def __getitem__(self, key):
		return key**2

foo = Foo()
print(foo[10]) # Give us 100 (getitem protocol it is how we get something using '[]')

# Just like this getitem protocol, just like this dictionary
# look up exists as an abstract protocol in Python so there
# is a function call protocol.

class Foo2():
	def __call__(self, val):
		return val**2

foo2 = Foo2()
print(foo2(10)) # Give us 100 (function call protocol it is how we get something using '()')

# Fundumentaly this is show us that everything in Python
# is an object. And that all Python objects respond to a
# same ... protocols. A regular function you may use in
# Python is the same you will use an object with the
# call method on it. There may be different
# implemantation, but behaviour should be identical.