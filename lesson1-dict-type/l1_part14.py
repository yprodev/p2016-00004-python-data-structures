# Let's talk what a dictionary really means. Let's talk about
# semantics behind the dictionary. Sometimes we have to use a
# lookup table.
sine = [-0.0000, -0.0495, -0.0988, -0.1479,
				-0.1966, -0.2449, -0.2925, -0.3394,
				-0.3855, -0.4307, -0.4748, -0.5177,
				-0.5594, -0.5997, -0.6386, -0.6758,
				 0.6758,  0.6386,  0.5997,  0.5594,
				 0.5177,  0.4748,  0.4307,  0.3855,
				 0.3394,  0.2925,  0.2449,  0.1966,
				 0.1479,  0.0988,  0.0495,  0.0000,]

from math import pi
angle = 0
print(angle)

angle_index = int((pi + angle) / (2 * pi) * len(sine))
print(angle_index) # 16th element in our sine table
print(sine[angle_index - 1]) # -0.6758


from math import sin
print(sin(angle))

print(sine[angle_index], sine[angle_index - 1]) # 0.6758, -0.6758 - These values surround the actual value that we want (0.0)


# What we could do we could create a dictionary that will
# represent a look up table given some input, providing the
# output value for that function.
table = {-3.1416: -0.0000, -3.0921: -0.0495, -3.0426: -0.0988, -2.9932: -0.1479,
					# I was too lazy to type all the numbers by myself
					2.9932:  0.1479, 	3.0426:  0.0988,  3.0921:  0.0495,  3.1416:  0.0000}

# Here is an example how we can do a linear interpolation
from bisect import bisect
# from __future__ import division

class interpolating_dict(dict):
	def __missing__(self, key):
		sorted_keys = sorted(self.keys())

		index = bisect(sorted_keys, key)

		if index == 0 or index == len(sorted_keys):
			raise KeyError('cannot extrapolate value {}'.format(key))

		left_key, right_key = sorted_keys[index - 1], sorted_keys[index]
		left_val, right_val = self[left_key], self[right_key]

		slope = (right_val - left_val) / (right_key - left_key)
		self[key] = value = slope * (key - left_key) + left_val
		return value

sine = interpolating_dict(table)
print(sine)

print(sine[3.1416])
print('Sin 0 -', sine[0])
print('Sin pi / 2 =', sine[pi / 2])
print(sine)



