# collections.deque
# ==================================================

tree = [('a', [('b', [('d', []),
											('e', [])]),
							 ('c', [('f', [])])])]

def preorder(tree):
	stack = [tree[0]]
	output = []
	while stack:
		value, children = stack.pop()
		output.append(value)
		stack.extend(reversed(children))
	return output

print(preorder(tree))


# ==================================================

from collections import deque

def levelorder(tree):
	queue = deque([tree[0]])
	output = []
	while queue:
		value, children = queue.popleft()
		output.append(value)
		queue.extend(children)
	return output

print(levelorder(tree))


# ==================================================

from collections import deque
from string import ascii_lowercase

def palindrome(sentence):
	letters = deque()

	for char in sentence:
		char = char.lower()
		if char in ascii_lowercase:
			letters.append(char)

	while len(letters) > 1:
		if letters.popleft() != letters.pop():
			return False

	return True


print(palindrome("madam, i'm adam"))
print(palindrome("a man, a plan, a canal: suez!"))
print(palindrome("a man, a plan, a canal: panama!"))























