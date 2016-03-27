# Corner Cases
# ==================================================
some_tuple = (1, 'a', [])
print(some_tuple[2])

# We gonna add to this list an element two
try:
	some_tuple[2] += [2] # We will get an error
except:
	KeyError ("lalal")

# We will get an error, but we also will change the tuple item
print(some_tuple) # (1, 'a', [2])


