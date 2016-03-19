# Vigenere Cipher

'''
Plain text: 	attackatdawn
Key:					python
Cipher text:	prmhqxprwhka

	We start with a table:

		#				a b c d e f g h i ...
		#			------------------------
		#	a |		b c d e f g h i j ...
		# b |		c d e f g h i j k ...
		# c |		d e f g h i j k l ...
		# d |		e f g h i j h l m ...
		# ...
		#

	In this process we wanna select the corresponding row,
	then map from the unencoded letter to the encoded letter.

	So, we should have a dictionary that looks something like
	this:

CODEBOOK = {
	'a': {'a': 'b',
				'b': 'c', # ...
			 },
	'b': {'a': 'c',
				'b': 'd',
			 },
}

print(CODEBOOK['a']['b'])


	We could create this big table using dictionaries manually,
	but there is an easy way to do it faster.

'''

# ==================================================
# We can import ascii_lowercase string module which will give us
# a string containing all the letters.
from string import ascii_lowercase

# ==================================================
# Using that we can use this DICT COMPREHENTION syntax. This will
# corresponde to the rows of an empty dictionary.
'''
CODEBOOK = {x: {} for x in ascii_lowercase}
print(CODEBOOK)

'''

# ==================================================
# Then we need to use dict comprehension syntax inside empty dicts
# to create subdictionary.
'''
CODEBOOK = {x: {y: None for y in ascii_lowercase} for x in ascii_lowercase}
print(CODEBOOK)

'''

# ==================================================
# We can see that in the table letters are shifted to the left
# by one position. That is we are going to implement. Instead of going through
# ascii_lowercase we are going to enumerate ascii_lowercase. We are going to
# take an index of the each letter.

'''
CODEBOOK = {x: {y: None for y in ascii_lowercase} for i, x in enumerate(ascii_lowercase)}
print(CODEBOOK)

'''

# ==================================================
# And what we can do it is we can map y to the element of the ascii_lowercase
# that is equal to the element we are looking at (j) plus offset (i).
# The offset is increasing for each letter through enumerating. We may affect
# +1 to make sure that we are always offset.


# CODEBOOK = {x: {y: ascii_lowercase[(j + i + 1) % len(ascii_lowercase)]
# 									 for j, y in enumerate(ascii_lowercase)
# 							 }
# 								 for i, x in enumerate(ascii_lowercase)
# 					 }
# print(CODEBOOK)


# ==================================================
# We can write this code in the different formulation. We may use islice and cycle
# in order to first create an infinite cycling of ascii_lowercase and then
# just offset it by 'i' each time. This will prevent of using module (%)
# operation or index calculation (j + i + 1). We can take ascii_lowercase
# and it's ziped version of ascii_lowercase (islice(cycle(ascii_lowercase), i, None)).

'''
from itertools import islice, cycle

CODEBOOK = {x: {y: z for y, z in zip(ascii_lowercase, islice(cycle(ascii_lowercase), i, None))}
							 for i, x in enumerate(ascii_lowercase)}
print(CODEBOOK)

'''


# ==================================================
# The next step we will need in order to solve this problem is we'll need to
# strip the message to the things that can be encoded. So, for the message
# that contained 'a b c 1 2 3' we can't really encode '1 2 3'. We also can't
# encode the spaces, because it is also not a part of our codebook.

'''
message = 'a b c 1 2 3'
message = ''.join(m for m in message.lower() if m in CODEBOOK)
print(message) # 'abc'

'''

# ==================================================
# Bringing this together we have our solution here.

from string import ascii_lowercase
from itertools import repeat, cycle, islice

CODEBOOK = {x: {y: z for y, z in zip(ascii_lowercase, islice(cycle(ascii_lowercase), i, None))}
							 for i, x in enumerate(ascii_lowercase)}

def enchipher(message, key, codebook=CODEBOOK):
	# Strip out all the letters from our message
	message = ''.join(m for m in message.lower() if m in codebook)
	# Then cycle our key an infinite number of times and take out the
	# corresponding letter of the key (k) and use that to index the
	# row ([k]). Take out the corresponding letter of a message (m) and
	# use that to index into the look up table for that row ([m]).
	return ''.join(codebook[k][m] for k, m in zip(cycle(key), message))

def decipher(message, key, codebook=CODEBOOK):
	# Decodebook will iterate through the items in the codebook (in codebook.items())
	# to get a key (x) and the value (yz). The key is corresponding to the row and
	# the value should be a dictionary with that mappings with some input character
	# and some output character. Will iterate through all that item in that mapping
	# (yz.items()) and all we would do is swap them (z: y)
	decodebook = {x: {z: y for y, z in yz.items()} for x, yz in codebook.items()}
	# The deciphering looks exactly as a ciphering. We cycling our keys for the
	# infinite number of times and then we just look up for row and look up
	# within the row.
	return ''.join(decodebook[k][m] for k, m in zip(cycle(key), message))

# ==================================================
# Here we can see this code in action.
msg = 'Attack at dawn'
key = 'python'
enc_msg = enchipher(msg, key)
print(enc_msg) # encoded

print(decipher(enc_msg, key)) # unencoded




















