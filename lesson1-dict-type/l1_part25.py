# Concordance (Word Count)

'''
	Find the most commonly used words in the text file.

	If you are using UNIX OS run this command to download the text file.
		! head -n 10 paradise-lost.txt

	To be sure that everything works properly run the next code using
	downloaded file.

		with open('paradise-lost.txt') as f:
			text = ''.join(f)

		text[:50]

	To remove the byte order marker that will be at the first line
	of our document we can use encoding argument.

		with open('paradise-lost.txt', encoding='utf-8-sig') as f:
			text = ''.join(f)

'''

def concordance(text):
	freq = {}										# Creating an empty dictionary
	for word in text.split():		# Splitting text into words
		for word not in freq:			# Checking if word is NOT in our dictionary
			freq[word] = 0					# if NOT add word and assing 0 to it
		freq[word] += 1 					# if it is add 1 to the assigned value
	return freq									# return our dictionary with values

print(concordance(text))


# ==================================================
# But there will be some problems. Some word can be splited with
# punctuation signs. Some words we want to be with all letters in
# lowercase. We can fix this by adding one row.

'''
from re import sub

def concordance1(text):
	freq = {}																	# creating an empty dictionary
	for word in text.split():									# splitting text into words
		word = sub('[^\w]', '', word.lower())		# we make the word lowercase and use regexp to substitude all elements that are not a word
		for word not in freq:										# checking if word is not in our dictionary
			freq[word] = 0												# if not add word and assing 0 to it
		freq[word] += 1 												# if it is add 1 to the assigned value
	return freq																# return our dictionary with values

freq = concordance1(text)
# we can pull out the items (freq.items())
# here we are sorting items by there value (kv[1]).
# we can sort them in the reverse order.
# and we can index to find the top ten ([:10]).
# and we will get the list of tuples.
print(sorted(freq.items(), key=lambda kv: kv[1], reverse=true)[:10])

'''

# ==================================================
# But could we improve this code?

from re import sub

def concordance1(text):
	freq = {}
	for word in text.split():
		word = sub('[^\w]', '', word.lower())
		freq[word] = freq.setdefault(word, 0) + 1 	# We can do our code better just using setdefault method
		# We also may use here .get
		# freq[word] = freq.get(word, 0) + 1
		# Preferably we should use here .get

		# Also, we can't use here code like this:
		# freq.setdefault(word, 0) += 1
		# Because the result of this operation is integer that is
		# immutable type. So, we should record the result
		# in a variable and rewrite it everytime simultaneously.
	return freq

freq = concordance1(text)
print(sorted(freq.items(), key=lambda kv: kv[1], reverse=true)[:10])


# ==================================================
# We saw the defaultdict. We said that the defaultdict is a subclass
# of dict where you provide it a default initializer.
from collections import defaultdict

x = defaultdict(int) # int in this case a default initializer
print(x[1]) # 0

# This will provide us a zero valued or empty instance. x[1] will
# automaticly initialize the value of the key one to the value 0.

# If we type in any other arbitrary key it will initialize this.
print(x['jdkfjjdof']) # 0
print(x[2])
print(x) # We will get defaultdict(<class 'int'>, {2: 0, 'jdkfjjdof': 0})


# ==================================================
# We can use that in our concordance.

from re import sub
from collections import defaultdict

def concordance2(text):
	freq = defaultdict(int) 										# Here we will use our defaultdict
	for word in text.split():
		word = sub('[^\w]', '', word.lower())
		freq[word] += 1 													# .. and make shorter this line of code
	return freq

freq2 = concordance2(text)
print(sorted(freq.items(), key=lambda kv: kv[1], reverse=true)[:10])


# ==================================================
# And we can make this code even shorter. If we look at a collections
# module we will see something called Counter. Counter is our way to
# count elements in some collection. If we call Counter with the
# string we will get:
from collections import Counter
print(Counter('aabbbc')) # {'b': 3, 'a': 2, 'c': 1}

# ==================================================
# Thus we can use Counter in order to implement concordance in the
# single line. We will take the text splitted on words and take
# the word and lowercase it. We will substitude everything in the
# word that is not a unicode letter with the blank space. And we
# will pass it to the Counter.

from re import sub
from collections import Counter

def concordance3(text):
	return Counter(sub('[^\w]', '', word.lower()) for word in text.split())

freq3 = concordance3(text)
print(sorted(freq.items(), key=lambda kv: kv[1], reverse=true)[:10])









