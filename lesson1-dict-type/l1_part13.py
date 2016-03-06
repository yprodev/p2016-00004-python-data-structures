# There is another way to create dictionaries in Python
# dict-comprehensions - this can lead to very idiomatic
# code. Often when we are creating a dictionary we may
# see that we populate the enties of a dictionary using
# a for loop. The dict-comprehension syntax allows us to
# write this for loop very [couldn't understande the word].

# When we are looking at the dict.copy() syntax we may be
# remind ourselves of our set builder notation. In our set
# builder notation we create a set by default defining a
# formula that describes the entries of that set. In our
# dict-comprehension syntax we have syntax that looks as
# like we defining a dictionary by describing content of
# that dictionary. Here we could see that we are creating
# a dictionary with a keys or elements 'x' and values of
# these 'x' elements squared. These elements are retrieved
# by iterating over the numbers from zero to ten (not
# including ten).
# {x: x**2 for x in range(10)}
print({x: x**2 for x in range(10)})

# We can also add a predicate
print({x: x**2 for x in range(10) if x%2 == 0})

# We may use this to implement a very simple substitution
# cipher. It is a way to encrypt some text by going trough
# each letter and performing substitution for each of
# these letters. In other words we may say that our cipher
# substitutes letter 'e' with letter 'l', letter 'i' with
# letter 'j', the letter 'y' with letter 'h'. We can use a
# dictionary and dict comprehentions to do it very convinient.


# Let's start from importing a module.
from string import ascii_lowercase
print(ascii_lowercase) # we will get a set of ascii lowercase letters


# We can shuffle these letters
from random import shuffle
# print(shuffle(ascii_lowercase))
# ERROR, because we can use shuffle() to a string, because string is unmutable type


# What we have to do is to assign the letters to a list
# and then shuffle a list.

alphabet = list(ascii_lowercase)
# print(alphabet) # Just alphabet list

# shuffle(alphabet)
# print(alphabet) # We must see shuffled list


# And what we can then do is use our dictionary comprehension
# syntax in order to create a dictionary that maps a from the
# original letter to the encoded one. What we will do is we'll
# iterate over all the letters in ascii_lowercase - from 'a'
# to 'z'. And then we just pop elements from our randomly
# shuffled list. When we do that we end up with code book.
codebook = {x: alphabet.pop() for x in ascii_lowercase}
print('Our codebook', codebook)

# We can take a message
message = 'python is great!'

# And we can use our generator expression syntax in order to
# iterate through the elements of the string and to map them
# with our code. We can use .get() method, because some
# elements of the string may not be part of our codebook.
# Nameless spaces and punctuation may not be part of the
# codebook. Thus we end up with code like this:

encoded = ''.join(codebook.get(m, '') for m in message)
# iterate through elements in messege string, look up for that
# letter in our codebook and replace it with it's corresponding
# letter in our codebook. If that letter is not part of our
# codebook we will replace it with our empty string. We create a
# string of letters and we will join them to a new string.
print(encoded)
# Note that spaces are removed and punctuation is removed


# We could create a reverse codebook using our dict-comprehension
# syntax. This is you may see very often. Sometimes we wonna to
# create a reverse map. Ofcourse as we've noted before the dictionary
# does not required that the values be unique. Dictionary type requires
# that the keys be unique, the values can repeat. In order to provide
# a reverse mapping we must have a guarantee that the original mapping
# had a unique value for each key. In this particular case that happens
# to be true. The keys in this codebook are unique and the values in
# our codebook are unique. There is no letter that maps to multiple
# resulting letters and there is no resulting letter that comes from
# multiple original letters. So we can reverse this mapping by just
# iterating through the items in the codebook and creating a dictionary
# we will be reversed the key-value mapping to provide a value-key
# mapping.
reverse_codebook = {v: k for k,v in codebook.items()}
print('reversed codebook', reverse_codebook) #### !!! Not working like in the tutorial !!!
#### But code is working. May be problem in the interpreter.


# We can take our encrypted message and pass it through our reversed
# codebook in order to decode that message. Notice, as we said before
# spaces and punctuation are being removed.

print(''.join(reverse_codebook.get(m, '') for m in encoded))