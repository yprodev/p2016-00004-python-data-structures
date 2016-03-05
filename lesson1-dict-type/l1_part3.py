# Dictionary as a MAP
# In C++ and Java there are datatypes are called MAPS

# Here we are creating two dictinaries
# As you can see the keys are unique but the values can be repeated

course_professors = {
											'calculus': 'Prof. Kotter',
											'diff eq': 'Prof. Fenny',
											'linear algebra': 'Prof. Kotter',
											'real analysis': 'Prof. Crabtree'
}

'''
student_courses = {
										'vinnie': ['calculus', 'diff eq'],
										'arnold': ['calculus', 'linear algebra'],
										'juan luis': ['real analysis']
}

'''
# Here we are using SETS inside of dictinaries
# A set just like the dictionary and the every element of the set must be unique
# But the set has no corresponding value (like key in dictionary)
student_courses = {
										'vinnie': {'calculus', 'diff eq'},
										'arnold': {'calculus', 'linear algebra'},
										'juan luis': {'real analysis'}
}

# Now we are going trying to create a new map

student_professors = {} # Which student has which professor

for student in student_courses: # Every entry in student_courses
	for course in student_courses[student]: # Every entry from the SET of values according to the exact student
		if student not in student_professors: # If this student is now not in the student_professor dictionary
			student_professors[student] = set() # Add this student to this dictionary and assign fot him a set
		student_professors[student].add(course_professors[course]) # If we have student in this dict add professors name in early created set according to the courses this student has

print(student_professors)