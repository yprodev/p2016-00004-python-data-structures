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
# print(deck1)


# Example and Valid Straights
# ==================================================
# Let's take a look at how to score hands in the simple pocker game.
# Insread of using the set of strings we are going to use the set of
# tuples. We will use the name tuple data type from our collections
# module and that way we will be able to pull out from a card of it's
# suit and it's rank.
from collections import namedtuple

Card = namedtuple('Card', 'suit rank')
deck2 = {Card(suit, rank) for rank in numbers | faces
													for suit in suits}

# print(deck2)

# ==================================================
# How we can implement a function that can determine the given hand
# represent different combinations.
'''
		- straight flush
		- four of a kind
		- full house
		- flush
		- straight
		- three of a kind
		- two pair
		- one pair
		- high card


		valid_straights = {set(range(n, n+5)) for n in range(2,7)}

		We will get an error here.

		'''
# The set-type happens to be mutable. And one common correspondens
# that we have in Python is that all of our mutable built-in types
# are not hashable. As a concicuance we can not create a set of
# sets. Because the elements of the set will not be would not be
# hash. However, we will provide the easy workaround for this. In
# addition for our set-type in Python we also provide with a
# frozen set-type. The main difference - once it was provided it
# can not be changed - it is frozen in place.

'''
valid_straights = {frozenset(range(n, n + 5)) for n in range(2,7)}
print(valid_straights)

'''

valid_straights = {frozenset(range(n, n + 5)) for n in range(2,7)} | \
									{frozenset(['ace', 2, 3, 4, 5])								 } | \
									{frozenset([7, 8, 9, 10, 'jack'])							 } | \
									{frozenset([8, 9, 10, 'jack', 'queen'])				 } | \
									{frozenset([9, 10, 'jack', 'queen', 'king'])	 } | \
									{frozenset([10, 'jack', 'queen', 'king', 'ace'])	 }

# print(valid_straights)


# Best Hand
# ==================================================
# Having set up helper functions and helper structions called
# valid_straights we now ready to write a fucntion called
# best hand that will evaluate the hand of cards we will give
# it. It will tell us the best hand according to the rules of
# pocker. That are contained within these cards.

from itertools import groupby, combinations

def best_hand(hand):

	# We are going to extract all the suits of all the cards
	# hand is expected to be a set or some other iterable of cards. Will iterate through the all
	# cards that we have and we will extract the suit for those cards. We will use the set
	# comprehension because we want each card to be represent just once.
	suits_in_hand = {card.suit for card in hand}
	ranks_in_hand = {frozenset(cs) for _,cs in groupby(sorted(hand, key=rank2value), key=rank2value)}

	high_card				 = best_card(hand)
	twos_of_a_kind	 = {cs for cs in ranks_in_hand in len(cs) == 2}
	threes_of_a_kind = {cs for cs in ranks_in_hand in len(cs) == 3}
	fours_of_a_kind	 = {cs for cs in ranks_in_hand in len(cs) == 4}
	straights				 = {cs for cs in combinations(hand, 5) if {c.rank for c in cs} in valid_straights}

	if len(suits_in_hand) == 1 and straights:
		return hand, 'straight flush'

	if fours_of_a_kind:
		return max(fours_of_a_kind, key=lambda cs: rank2value(best_card(cs))), 'four of a kind'

	if threes_of_a_kind and twos_of_a_kind:
		return max(threes_of_a_kind, key=lambda cs: rank2value(best_card(cs))) | \
					 max(twos_of_a_kind,	 key=lambda cs: rank2value(best_card(cs))), 'full house'

	if len(suits_in_hand) == 1:
		return hand, 'flush'

	if straights:
		return max(straights, key=lambda cs: rank2value(best_card(cs))), 'straight'

	if threes_of_a_kind:
		return max(threes_of_a_kind, key=lambda cs: rank2value(best_card(cs))), 'three of a kind'

	if len(twos_of_a_kind) == 2:
		return twos_of_a_kind.pop() | twos_of_a_kind.pop(), 'two pairs'

	if len(twos_of_a_kind) == 1:
		return twos_of_a_kind.pop(), 'one pairs'

	return {high_card,}, 'high card'


# Helper Functions
# ==================================================

def rank2value(card):
	if card.rank in numbers:
		return card.rank

	return {'ace': 		14,
					'king':		13,
					'queen':	12,
					'jack':		11,
				 }[card.rank]

def best_card(hand):
	return max(hand, key=rank2value)


# Example Hands
# ==================================================

# %%time # This never works in this course

from itertools import combinations

example_hands = {}

for hand in combinations(deck, 5):
	cards, hand_type = best_hand(hand)
	if hand_type not in example_hands:
		example_hands[hand_type] = cards, hand



# Displaying Example Hands
# ==================================================

for hand_type in example_hands:
	print(hand_type)
	print('=' * len(hand_type))
	matched_cards, all_cards = example_hands[hand_type]
	for cards in all_cards:
		print('   ', '*' if card in matched_cards else ' ', '{} of {}'.format(card.rank, card.suit))
