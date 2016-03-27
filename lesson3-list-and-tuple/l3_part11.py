# Argument Unpacking
# ==================================================
# *w take any additional argument that have not alrady matched
# to an existing positional argument

# def three_things(x, y, z, *w):
# 	print("I like three things: {}, {} and {}".format(x, y, z))

def three_things(x, y, z):
	print("I like three things: {}, {} and {}".format(x, y, z))

fruits = ['apple', 'banana', 'pear']
# This is unpacking syntax (*fruits).
print(three_things(*fruits))


# We will get en error because we are trying to pass four arguments
# when the function takes only three
# three_things(*['apple', 'banana', 'watermelon', 'strawberry'])


# ==================================================
def three_names(first, middle, last):
	print("I have three names: {}, {} and {}".format(first, middle, last))

profile = 'John', 'Quincy', 'Adams'
print(three_names(*profile))

# If we will pass too few or too many arguments we will get a type error


