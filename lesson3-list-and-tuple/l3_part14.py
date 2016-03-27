# Semantics
# ==================================================
presidents = [
	('George',				[],									'Washington', 1732, 1799, 1789, 1797,),
	('John',					[],									'Adams', 			1735, 1826, 1797, 1801,),
	('Thomas',				[],									'Jefferson',	1743, 1826, 1801, 1809,),
	('James',					[],									'Madison',		1751, 1836, 1809, 1817,),
	('James',					[],									'Monroe',			1758, 1831, 1817, 1825,),

	('John',					['Quincy'],					'Adams',			1767, 1848, 1825, 1829,),
]


pres_ages = []

for pres in presidents:
	first, middle, last, born, died, took, left = pres
	pres_ages.append(('{} {}'.format(first, last), took - born))

pres_ages.sort(key=lambda item: item[1])
print(pres_ages)

for name, age in pres_ages:
	print('{:<25} {}'.format(name, age))

print('================================================================')

# We can see the 5 last elements
for name, age in pres_ages[-5:]:
	print('{:<25} {}'.format(name, age))

print('================================================================')

# We can see the 10 youngest presidents
for name, age in pres_ages[-5:]:
	print('{:<25} {}'.format(name, age))