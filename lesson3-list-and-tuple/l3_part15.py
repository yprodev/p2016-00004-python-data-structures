# collections.namedtuple
# ==================================================
from collections import namedtuple
# Two types of syntax
# You may name fields names within a string or use list
President = namedtuple('President', ['first', 'middle', 'last', 'born', 'died', 'took', 'left'])
President = namedtuple('President', 'first middle last born died took left')

presidents = [
	President('George',				[],									'Washington', 1732, 1799, 1789, 1797,),
	President('John',					[],									'Adams', 			1735, 1826, 1797, 1801,),
	President('Thomas',				[],									'Jefferson',	1743, 1826, 1801, 1809,),
	President('James',					[],									'Madison',		1751, 1836, 1809, 1817,),
	President('James',					[],									'Monroe',			1758, 1831, 1817, 1825,),

	President('John',					['Quincy'],					'Adams',			1767, 1848, 1825, 1829,),
]

print(presidents[0])
print(type(presidents[0])) # class __main__.President

pres_ages = []

for pres in presidents:
	if pres.left and pres.died:
		pres_ages.append((pres, pres.died - pres.left))
	elif pres.left:
		pres_ages.append((pres, 2015 - pres.left))

pres_ages.sort(key=lambda item: item[1], reverse=True)

for pres, age in pres_ages:
	name = ' '.join([pres.first] + pres.middle + [pres.last])
	print('{:<35} {}'.format(name, age))


%matplotlib inline

from matplotlib.pyplot import hist
ages = [age for pres, age in pres_ages]
hist(ages, bins=35, cumulative=-1)