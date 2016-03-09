# Rangedict and Passthrudict
# Some interesting things we can do, using __missing__
# We are going to implement something that is very
# similar to a dictionary, with very similar semantics
# that is not a total pro version of getitem protocol.
# So one thing we've already discussed is a dictionary
# in the form of a ... addressable or assosiative array.
# Namely that we can view a dictionary as some amount of
# memory or we can look something up by it's content. We
# can assosiate some value with other values.

from collections import Iterable

class rangedict(dict):
	def __missing__(self, key):
		for k, v in self.items():
			if isinstance(k, Iterable):
				left, right = k
				if left <= key < right:
					self[key] = v
					return v
		raise KeyError('cannot find {} in rangedict'.format(key))

codes = rangedict({(	0, 		10): 'red',
									 ( 10, 	 100): 'yellow',
									 (100,	1000): 'green',})

print(codes[30]) # yellow
print(codes[105]) # green
print(codes)
print(codes[5]) # red
print(codes)

# Everytime we are trying to find new key, we are
# rebuilding the whole dictionary.


# Namely, here we look up the key at the dictionary and if the
# key does not exist we just return the key. And we can use
# this to implement something looks kind of like censorship
# machanism.
class passthrudict(dict):
	def __missing__(self, key):
		return key

censor = passthrudict({'hell': 'he**',
											 'darn': 'd*rn',})

sentence1 = 'That darn cat!'
print(' '.join(censor[w] for w in sentence1.split()))
sentence2 = 'Y\'all can go to hell; I\'m going to Texas!'
# will not replace 'hell' word
print(' '.join(censor[w] for w in sentence2.split())) # this pass through because after the word we can see ';' - semicolon



# Example 2
# we need to install all these modules
from intertools import groupby, chain
from unicodedata import category

# instead of the default split method we could use our fancy
# split method.
def fancy_split(s):
	# Here we get the string and group string by unicode category (L - Letters)
	# then we will join the string again.
	return [''.join(g) for k, g in groupby(s, key=lambda x: category(x)[0] == 'L')]

sentence3 = 'Y\'all can go to hell; I\'m going to Texas!'
print(fancy_split(sentence3))





