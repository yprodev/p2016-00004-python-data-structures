# dict methods
# We could use dir() method to see all the methods the exact data type provides
# print(dir({})) # What methods provides dictionaries

# We want to create a list and go through the each element to pull out
# values without underscores
print([attr for attr in dir({}) if '__' not in attr])

# We will concentrate on these methods that this code gives us
# We are going to use dictionaries idiomaticly