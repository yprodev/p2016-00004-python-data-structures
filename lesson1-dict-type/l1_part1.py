# PROBLEM STATEMENT: Vigenere Cipher
# Vigenere Cipher is a very famous classical encryption algorithm.
# It is very good statement to use dictionaries in Python to write
# idiomatic code.

# Plain text: attackatdawn
# Key: python
# Cipher text: prmhqxprwhka

from string import ascii_lowercase
from itertools import repeat, cycle, islice

CODEBOOK = {x: {y: z for y,z in zip(ascii_lowercase, islice(cycle(ascii_lowercase), i, None))}
						for i, x in enumerate(ascii_lowercase)}

def encipher(message, key, codebook=CODEBOOK):
	message = ''.join(m for m in message.lower() if m in codebook)
	return ''.join(codebook[k][m] for k, m in zip(cycle(key), message))

def decipher(message, key, codebook=CODEBOOK):
	decodebook = {x: {z: y for y, z in yz.items()} for x, yz in codebook.items()}
	return ''.join(decodebook[k][m] for k, m in zip(cycle(key), message))

# msg = 'Attack at dawn!'
# key = 'python'
# enc_msg = encipher(msg, key)
# enc_msg
# And we will get encrypted message - 'prmhqxprwhka'

# decipher(enc_msg, key)
# And we will decript the message and get - 'attackatdawn'



########################################################################################################

# PROBLEM STATEMENT: Concordance (Word Count)
# This is very common interview question and it often called word count.
# We are going to find the 10 most commonly used words in the text file.

# wget -O paradise-lost.txt 'http://www.gutenberg.org/cache/epub/26/pg26.txt'
# head -n 10 paradise-lost.txt

from re import sub

def concordance(text):
	freq = {}
	for word in text.split():
		word = sub('[^\w]', '', word.lower())
		if word not in freq:
			freq[word] = 0
		freq[word] += 1
	return freq

with open('paradise-lost.txt') as f:
	text = ''.join(f)

freq = concordance(text)
sorted(freq.items(), key=lambda kv: kv[1], reverse=True)[:10]

# The top ten words
# [('and', 3483),
#		('the', 3161),
#		('to', 2326),
#		('of', 2186),
#		('in', 1430),
#		('with', 1208),
#		('his', 1181),
#		('or', 795),
#		('that', 720),
#		('all', 712)]








