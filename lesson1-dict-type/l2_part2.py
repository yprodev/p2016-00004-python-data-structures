# Let's start with the most obvious term - DICTIONARY

# In this example the keys are strings and the values are strings
dictionary = {
	'one': 'uno',
	'two': 'dou',
	'three': 'tres'
}

# To execute needed value we use square brackets
print(dictionary['one']); # uno


''' We can not do it in the reverse order'''
# print(dictionary['uno']); # We will get an error Traceback

'''
		We will got the same error when we try to get the key
		that does not exists.

'''
# print(dictionary['four']); # We will get an error Traceback


# We can assign a value to the dictionary
dictionary['four'] = 'quatro'
print(dictionary);

# We also can remove entry in the dictionary
del dictionary['one']
del dictionary['three']
print(dictionary);
