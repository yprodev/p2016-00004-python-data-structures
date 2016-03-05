# The dictionary contains a set types values
# so items in the set can not be repeated.
# Sets have the same properties as dictionaries.

student_courses = {
										'vinnie': {'calculus', 'diff eq'},
										'arnold': {'calculus', 'linear algebra'},
										'juan luis': {'real analysis'}
}

student_courses['vinnie'].add('linear algebra')

print(student_courses)

# Lets add 'linear algebra' course for another student. Note that
# freddie is not a key in our dictionary.

# student_courses['freddie'].add('linear algebra')
# And we will get an error. So, we need to initialize a set for
# this new student.
if 'freddie' not in student_courses:
	student_courses['freddie'] = set()
student_courses['freddie'].add('linear algebra')

# This code we are using very commonly. So the python provides a method
# for these kind of things. .setdefault() method corresponding to a key
# if that key does not in the dictionary then it will initialize that
# key to a default value and the return value would be eigther existing
# value for that key or the new value, you've just set. Thus, we could
# take those three line (if statement) and rewrite them in one line.

# if rosalie is not part of the dictionary create a set. If rosalie is
# part of this dictionary then we just retrieve the value corresponding
# to that key. And then once we have that we'll add to it one course.
student_courses.setdefault('rosalie', set()).add('calculus')
print(student_courses)
student_courses.setdefault('rosalie', set()).add('linear algebra')
print(student_courses)
