# Additional Methods
# ==================================================

'''
	.clear
	.difference
	.difference_update
	.intersection
	.intersection_update
	.symmetric_difference
	.symmetric_difference_update

'''

# ==================================================
# Let's take a look at the clear method
animals = {'dog', 'cat', 'bird'}
print(animals)

# animals.clear()

# We can remove the set in another way
while animals:
	animals.pop()

print(animals)



# ==================================================
# .difference
# The minus (-) operator will also perform a set difference operator
print({'dog', 'cat', 'bird'} - {'dog'}) # like using difference method

# If the element does not in this set the behaviour should be predictable
print({'dog', 'cat', 'bird'} - {'horse'}) # Nothing will happen

# The arguments of the difference method should be another set
print({'dog', 'bull', 'cat'}.difference('cat')) # this is not a set argument
print({'dog', 'bull', 'cat'}.difference({'cat'})) # it's OK
print({'dog', 'bull', 'cat'}.difference(['cat'])) # list is also OK


# Note, that sometimes we want to find the elements that are unique for
# each set. So we may wanna find the symmetric difference. We may wanna
# find the elements when you subtrack one set from the other and subtrack
# in the reverse order the other set from the first and union those results.
# We will see the elements that are unique for each different set.

print({'dog', 'bird', 'cat', 'horse'}.symmetric_difference({'dog', 'horse', 'giraffe'})) # {'bird', 'cat', 'giraffe'}

# We can also use a carret (^) to get the behaviour of symetric difference
print({'dog', 'bird', 'cat', 'horse'} ^ {'dog', 'horse', 'giraffe'}) # {'bird', 'cat', 'giraffe'}



# ==================================================
# .intersection
# Will show us the elements that share between two sets.
print({'dog', 'bird', 'cat', 'horse'}.intersection({'dog', 'horse', 'giraffe'})) # {'horse', 'dog'}

# The same behaviour we can reach using the AND (&) operator.
print({'dog', 'bird', 'cat', 'horse'} & {'dog', 'horse', 'giraffe'}) # {'horse', 'dog'}


# ==================================================
# .intersection_update
animals = {'dog', 'bird', 'cat'}
animals.intersection_update({'bird', 'horse'})

# The same when use:
# animals &= {'bird', 'horse'}
print(animals) # {'bird'}



# .difference_update
animals = {'dog', 'bird', 'cat'}
animals.difference_update({'bird', 'horse'})

# The same when use:
# animals -= {'bird', 'horse'}
print(animals) # {'cat', 'dog'}



# .update
animals = {'dog', 'bird', 'cat'}
animals.update({'bird', 'horse'}) # think 'union_update'

# The same when use:
# animals |= {'bird', 'horse'}
print(animals) # {'cat', 'dog', 'bird', 'horse'}



# .symmetric_difference_update
animals = {'dog', 'bird', 'cat'}
animals.symmetric_difference_update({'bird', 'horse'})

# The same when use:
# animals ^= {'bird', 'horse'}
print(animals) # {'cat', 'dog', 'horse'}











