# The Set Type

'''
	- collection of items
	- no natural sorting
	- unique items
	- hashability
	- methods: intersect, difference, union, ...

'''


# Interacting with the set-type
# ==================================================

suits = {'hearts', 'diamonds', 'spades', 'clubs',} # This is a LITERAL syntax
faces = set(['ace', 'king', 'queen', 'jack']) # This is a VALUE CONSTARACOR
numbers = set(range(2, 11))

# If we add a duplicate the value constractor will delete the duplicate
# in order to save only unique values.
# faces = set(['ace', 'king', 'queen', 'jack', 'jack'])

print(suits)
print(faces)
print(numbers)

# ==================================================

deck = set() # {} means 'empty dictionary'. To create an empty set we should use set()

for suit in suits:
	for number in numbers:
		deck.add('{} of {}'.format(number, suit))
	for face in faces:
		deck.add('{} of {}'.format(face, suit))

# print(deck)


# Indexing
# ==================================================

# print(deck[0]) # we will get a Type Error

# The set has no key value pair to get items from it.


# ==================================================
# The choice function from a random module is used in order to 
# randomly choose an element from some sequence.
'''
from random import choice
print(choice(deck))

'''
# Unfortunately we will see a TypeError. And it is the same error that
# we saw above. The set type does not support indexing. Unfortunately
# in the implementation of the choice function in the random module
# it assumes that we have the ability to index into the values of the
# collection that was provided.


# ==================================================
# Another very common operation that we want to perform on the deck of cards
# is to shuffle it. But we could also think that the shuffle operation
# is going to be implemented by randomly selected indexes and swaping
# elements by the indecies. As a consiquence shuffle function also
# will not work on a set type.
'''
from random import shuffle
shuffle(deck)

'''


# Iterate and Union
# ==================================================
# Let's just construct a hand of cards

'''
hand = set()

for card in deck:
	if len(hand) < 5:
		hand.add(card)
		deck.remove(card)

print(hand)

'''
# Here we will get a RunTimeError. One common mistake we may seen here
# is that we are iterating over the deck and manipulation over the deck
# when we are removing elements from it. So, we are going to get an
# error saying that we can't simultaneously go over the elements and
# also change the contents of the deck.


# ==================================================
# We just break it into two loops to construct our hand and a second loop
# we remove the cards from our deck that in our hand.

hand = set()

for card in deck:
	if len(hand) < 2:
		hand.add(card)

for card in hand:
	deck.remove(card)

# print(hand)

# ==================================================
# Here is another way that we can represent taking items out of the deck
# and putting that into some set representing either a hand or the cards
# that are put to the board.
board = set()

for _ in range(3):
	board.add(deck.pop()) # At each step will be pop the element of the deck (.pop() - remove and also return that remove item)

# print(board)


# ==================================================
# Now one thing that we might like to do when we are deciding how much we
# wanna bet is take in the consideration the cards both in our hand and
# the cards that are on the board. Because the hand that we construct
# will be construct from all of this cards. So, the first operation
# that we might wanna do in UNION two sets. We can perform a union operation
# in the set-type with two syntaxes.

# print(board | hand) # single pipe
# print(board.union(hand)) # union method




# Remove and Discard
# ==================================================
# Let's add a High Jocker and the Low Jocker
# deck.add('High Jocker')
# deck.add('Low Jocker')

# For the game like Poker we want to remove these cards
# deck.remove('High Jocker')
# deck.remove('Low Jocker')

# Remove operation has some differences with add operation.
# We can remove item from the set only once, instead of adding -
# we can add infinite number on times, but set will store only
# the unique values. If we try to remove something that is not
# currently in the set, we will get an Error.


# ==================================================
# This could be discard by the discard method. The discard method
# will remove the element from the set if that element does belong
# to the set and if the element doesn't happen to belong to the
# set it will perform no action.

deck.discard('rules of five cards stud')


# Comprehension
# ==================================================
# Let's use the SET COMPREHENSION SYNTAX in order to create another
# set.

deck1 = { '{} of {}'.format(rank, suit) for rank in numbers | faces 
																				for suit in suits }

deck1.update({'high Jocker', 'low Jocker'})
# It also could be a list
# deck1.update(['high Jocker', 'low Jocker'])
print(deck1)
