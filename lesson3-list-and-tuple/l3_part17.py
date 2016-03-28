# collections.deque
# ==================================================

def balanced(expr):
	groupings = { ')': '(',
								']': '[',
								'>': '<',
								'}': '{', }
	stack = []

	for char in expr:
		if char in groupings.values():
			stack.append(char)

		elif char in groupings:
			if not stack or stack.pop() != groupings[char]:
				return False

	return not stack


print(balanced('()'))
print(balanced('(()'))
print(balanced('(())'))
print(balanced('(([]))'))
print(balanced('(([{<>}]))'))
print(balanced('(([{>}]))'))