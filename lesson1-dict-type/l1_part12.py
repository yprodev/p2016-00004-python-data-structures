# There is very useful uderscore method that we should look at - dict.__missing__
# This method would be called internaly, when the key look up was failed.
# If you try to look up the key in the dictionary and that key does not exist
# and there is a method corresponding to __missing__ then this method would be
# called and will provided the key.
class lowercasedict(dict): # It inherits from dictionary - inherits all of the behaviour from the dictionary class
	def __missing__(self, key):
		# In that method if the key does not exist it will look up the lowercasing of that key
		return self[key.lower()]

# We can create the dictionary of this type and we can look up this
# dictionary normaly. However if we look up the element of this
# dictionary and that element does not exist then we look up lower
# casing that key that we provided.
d = lowercasedict({'uno': 'one', 'dos': 'two'})
print(d['uno']) # we know key
print(d['UNO']) # we use lowercasing look up
print(d['uNo']) # we use lowercasing look up

# Now we have a dictionary that is case insensitive

print(d.get('UNO', d.get('uno')))