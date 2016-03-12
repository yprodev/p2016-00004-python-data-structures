# Collections.Defaultdict

# As we look at the dictionary as a mapping we had an example
# that look something like this.

# student_courses = { 'vinnie': {'calculus', 'diff eq'},
# 										'arnold': {'calculus', 'linear algebra'},
# 										'juan luis': {'real analysis'}}

# Let's say we want to a linear algebra subject to a student
# freddie. But we are going to get an error.
# student_courses['freddie'].add('linear algebra')

# The problem is that the freddie is not the value in the
# dictionary. If we want this to work - we have first to add
# freddie to the top level dictionary.
# student_courses['freddie'] = set()
# student_courses['freddie'].add('linear algebra')


# INSTEAD we may go to the collections module and use a helper
# called a default dict. The defaultdict behaves like a
# dictionary, except when you trying to manupulate the entry
# that does not exist and it will materialize that entry, using
# some function that you provide it.

# Here we have a defaultdict that will create an empty set
# everytime we want to set something up.
from collections import defaultdict

student_courses = defaultdict(set)
student_courses.update({ 'vinnie': {'calculus', 'diff eq'},
										'arnold': {'calculus', 'linear algebra'},
										'juan luis': {'real analysis'}})

print(student_courses)

student_courses['freddie'].add('linear algebra')
print(student_courses)

student_courses['kotter']
print(student_courses)

student_courses['kotter'].add('calculus')
print(student_courses)

print('foobar' in student_courses) # False