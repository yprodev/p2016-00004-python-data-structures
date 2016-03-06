# as a relation or a function
'''
		VERY USEFUL LESSON - REVISE IT!
'''

# Implementation of a quadratic equation
# For the polynomial the highest degree is square such as x^2 + 2x + 1
# the coefitiances will be 1, 2 and 1. And it will give us (x + 1)(x + 1)
from math import sqrt
def roots(a,b,c):
	return (-b + sqrt(b**2 - 4*a*c)) / (2*a)

print(roots(1,2,1)) # -1.0


# And let's use __missing__ function
class rootdict(dict): #???
	def __missing__(self, key):
		a, b, c = key
		return (-b + sqrt(b**2 - 4*a*c)) / (2*a)

# Creating new entity using a class
d = rootdict()
print(d) # empty dictionary {}
print(d[1,2,1]) # -1.0


# Here we could see a little memoise function
from sys import version_info
assert version_info.major == 3 and version_info.minor >= 3, \
	'requires PEP 362; Python 3.3 or later; python.org/dev/peps/pep-0362/'

# We are creating a class called a dictionary.
from inspect import signature
class memoise(dict):
	def __init__(self, func):
		self.func, self.signature = func, signature(func)
	# When a key does not exist in a memoization
	# We actually just called the function with this
	# memoisation dict was called on.
	def __missing__(self, key):
		args, kwargs = key
		self[key] = self.func(*args, **dict(kwargs))
		return self[key]
	# Here was are really bluring the difference between a dictionary
	# and a function.
	def __call__(self, *args, **kwargs):
		key = self.signature.bind(*args, **kwargs)
		return self[key.args, frozenset(key.kwargs.items())]


# When we add this memoisation to a function by decorator syntax
# we will end up doing this wrap this function subsequent call of
# the set of an arguments will not invoke the computation again.
from time import sleep

@memoise
def roots(a,b,c):
	sleep(1)
	return (-b + sqrt(b**2 - 4*a*c)) / (2*a)

print(roots(1,2,1)) # This will take 1 second for computation
print(roots(1,2,1)) # This will take 0 second because of memoise class

# Let us look at roots
print(roots) # {((1,2,1), frozenset()): -1.0}