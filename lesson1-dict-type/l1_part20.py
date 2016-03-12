# as a hash
# We are reffering to a dictionary implementation. In Python the
# built-in dictionary type is implemented as a hash table. In
# other language such as C++ the standard dictionary a standard
# map type may be implemented in a different fashion, perhaps as
# a red-black tree. In other languages such as Java we may even
# be able to control the underlying implementation of your
# dictionary type. However in Python the standard built-in 
# dictionary type is ALWAYS a hash. Let's take a look of what
# that means.

# Let's start from revisiting an error that had seen previously.
# We had said that a dictionary is a set of keys and what those
# keys map to - the values. We have said the values can be of
# any type. But we have said that there was a restriction on the
# type of the keys. That a key can be a number, can be a string,
# but it can't be something like a list. We said that a distinction
# between these different types was about mutability or
# immutability. We said that immutable types are allowed to be the
# keys of a dictionary, where is mutable types are not.

# {[1,2,3]: 4} ---> we will get an error 'unhashable type'
# That means this type can not be a hash. The hash is a very
# special function. The hash function takes a value and then 
# produces a numeric value corresponding to the hash of that value.

# In the case to try to hash a list the reason this does not work is
# that the hash function is used for determining how we store and
# retrieve something from a dictionary. When we put something in the
# dictionary we record the hash of that and then we use the hash for
# look up.

# Instead of searching through every element of a dictionary
# sequentialy or neither just to see if the element exists, nor to
# find en element, we can implement a much more efficient mechanism,
# the time complexity of which may be constant rather then linear
# that looks up the entry by its hash.

# The problem is if we allow the keys of a dictionary to be a mutable
# type, then what happened if we change the type between we store as
# a key to when we retrieve it. The options to a mutable type are not
# to store a hash by value. Because the value of the mutable type can
# over time. So we will force the calculate the hash based on the
# identity - based on the identity of a list, the exact list of memory.
# Within this we provide problems on look up, because we need to have
# a copy of the exact list if we looking something up later. We could
# not create list with the same contents and concern it to be eqevivalent.

# As a consiquence of the semantics around using is mutable types as
# keys of dictionary are sufficiently complex that we have decided
# to disallow this. The keys of dictionary must be hashable types. They
# must be immutable types.

english = ['one', 'two', 'three']
spanish = ['uno', 'dos', 'tres']

# We want to find index of a particular value
# This will be a linear search
print(english.index('two')) # must be 1


# We can perform a simple translation
print(spanish[english.index('three')]) # tres

# We could improve this behaviour. We could store sorted lists of the English
# and the Spanish terms and we could use an algorithm like this binary search
# provided by the bisect module in order to look something up. This binary
# search should be logN time. So, when we look up two we do a binary search
# into a list of sorted English terms. And then we retrive from the list of
# sorted spanish terms.

from bisect import bisect_left

lookup = [en for en,es in sorted(zip(english, spanish))]
value = [es for en,es in sorted(zip(english, spanish))]

key = 'two'
print(value[bisect_left(lookup, key)]) # dos



# If we want to we could graph all three of these approaches.

hash(x)

from numpy import array, linspace
from numpy.random import choice, shuffle
from string import ascii_lowercase
from bisect import bisect_left

MAX_SIZE = 10**5

letters = array([c for c in ascii_lowercase])
words 	= choice(letters, size=(MAX_SIZE, 10)) # 10 characters in size
words 	= array([''.join(w) for w in words])

ns = linspace(1, MAX_SIZE, 500) # Here we create a linear space from 1 to MAX_SIZE with 500 samples
list_times = []
dict_times = []
bisect_times = []

for n in ns:
	shuffle(words)

	sample_list = list(words[:n])
	sample_dict = dict.fromkeys(sample_list)
	sample_bisect = sorted(sample_list)

	lookup_words = choice(sample_list, size=10) # Here we choose 10 words to look up

	list_time 	= % timeit -q -n1 -o [sample_list.index(w) for w in lookup_words] # list mechanism
	dict_time 	= % timeit -q -n1 -o [sample_dict[w] for w in lookup_words] # dict mechanism
	bisect_time 	= % timeit -q -n1 -o [bisect_left(sample_bisect, w) for w in lookup_words] # bisect mechanism

	list_times.append(list_time.best)
	dict_times.append(dict_time.best)
	bisect_times.append(bisect_time.best)

% matplotlib inline

from matplotlib.pyplot import figure, plot, title, legend, ylabel, xlabel, show

fig = figure(figsize=(12,8))

plot(ns, list_times, 'bo', label=u'list lookup ~ O(n)')
plot(ns, dict_times, 'go', label=u'dict lookup ~ O(1)')
plot(ns, bisect_times, 'ro', label=u'bisect lookup ~ O(log(n))')

title('list vs dict vs bisect (binary search) lookup')
legend(loc='best')
xlabel('input size (elements)', figure=fig)
ylabel('best time out of 3 (s)', figure=fig)
show()
