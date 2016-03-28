# heapq module
# ==================================================

from random import randrange

numbers = [randrange(0, 100) for _ in range(10)]
print(numbers)


# ==================================================

from heapq import heapify

heapify(numbers)
print(numbers)


# ==================================================

from heapq import heappush

heappush(numbers, 55)
print(numbers)


# ==================================================

from heapq import nsmallest, nlargest

nlargest(3, numbers), nsmallest(3, numbers)


# ==================================================

from heapq import heappop

while numbers:
	print(heappop(numbers))







