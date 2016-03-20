# Prime number generator
# ==================================================
'''
	Find all the prime numbers up to a given number


def primes(max_num=100):
	found_primes = {2}
	for num in range(3, max_num):
		# determine if the number is prime
		pass
	return found_primes

print(primes())

'''

'''
def primes(max_num=100):
	found_primes = {2}
	for num in range(3, max_num):
		isprime = True
		for divisor in found_primes:
			if num % divisor == 0:
				isprime = False
		if isprime:
			found_primes.add(num)
	return found_primes

print(primes())

'''

'''
def primes(max_num=100):
	found_primes = set()
	for num in range(2, max_num):
		if not any(num % divisor == 0 for divisor in found_primes):
			found_primes.add(num)
	return found_primes

print(primes())

'''

'''
def primes(max_num=100):
	numbers = set(range(2, max_num))
	nonprimes = set()
	for num in numbers:
		for x in range(num, max_num // num + 1):
			nonprimes.add(num * x)
	return numbers - nonprimes

print(primes())

'''

'''
def primes(max_num=100):
	numbers = set(range(2,max_num))
	nonprimes = set()
	for num in numbers:
		nonprimes.update(num * x for x in range(num, max_num // num + 1))
	return numbers - nonprimes

print(primes())

'''


'''
def primes(max_num=100):
	numbers = set(range(2,max_num))
	for num in range(2, max_num):
		for x in range(num, max_num // num + 1):
			numbers.discard(num * x)
	return numbers

print(primes())

'''

'''
from itertools import count

def primes():
	found_primes = {2}
	yield 2 # yield statement produce value from this generator
	for num in count(3):
		isprime = True
		for divisor in found_primes:
			if num % divisor == 0:
				isprime = False
		if isprime:
			found_primes.add(num)
			yield num

'''

# list(primes())

'''
from itertools import islice

print(list(islice(primes(), 0, 10)))
print(set(islice(primes(), 0, 10)))

'''

from intertools import count

def primes():
	multiples = {}
	for num in count(2):
		print(multiples)
		if num in multiples:
			for x in multiples[num]:
				multiples.setdefault(num + x, set()).add(x)
			del multiples[num]
		else: # prime /
			multiples[num * num] = {num}
			yield num

from itertools import islice

print(list(islice(primes(), 0, 10)))




