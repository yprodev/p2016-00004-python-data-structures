# Comprehension syntax or generator expressions
# ==================================================

squares = [x**2 for x in range(10)]
print(squares)

even_squares = [x**2 for x in range(10) if x**2 % 2 == 0]
print(even_squares)

# NO SUCH thing as a tuple-comprehension
squares2 = (x**2 for x in range(10))
print(squares2)

squares3 = tuple(x**2 for x in range(10)) # this will work
print(squares3)
