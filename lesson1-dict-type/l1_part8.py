# We know that there is an error when we want to retrieve the
# DEFAULT key value pair when the key does not exists.
# So we can write some helper function

'''

def get_word(d, word):
	if word in d:
		return d[word]
	return None

'''

xs1 = {'one': 'uno'}
# We can expand this code to add the default value
def get_word(d, word, default=None):
	if word in d:
		return d[word]
	return default

print(get_word(xs1, 'two')) # None
# Reassign the default
print(get_word(xs1, 'two', 'dos')) # dos

# There is a built in method - .get()
# You can get the value of the dictionary by providing the key
# and then provide a default value if this key is not in the
# dictionary.
print(xs1.get('one', 'unknown')) # uno
print(xs1.get('two', 'unknown')) # unknown


# Let's say that we wonna see the length of a string that belongs
# to the dictionary.
'''
english_word = 'two' # Because the 'two' word is not in the dictionary
spanish_word = xs1[english_word] # We will see the error on this line, so we need to avoid this exception
len(spanish_word) # We will see the type error here, but the real error will be on the previous line

'''

# What is going to happen? .get() will return a None.
english_word1 = 'two'
spanish_word1 = xs1.get(english_word1, '') # Here we provide a default to avoid an error
len(spanish_word1)
