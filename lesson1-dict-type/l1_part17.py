# Dict-Alikes

from contextlib import closing
# You will need to install this module to run program
from pandas import HDFStore, DataFrame
from numpy import linspace

df = DataFrame() # Constructing a pandas data frame
df['val'] = linspace(0, 10**4, 10000) # Set a number of columns equal to from 0 to 10^4 with 10000 samples inside

with closing(HDFStore('test.hd5')) as store: # then we gonna save this to HDFStore
	display(store)
	# display(store['key'].head())
print(df)


from IPython.display import display

with closing(HDFStore('test.hd5')) as store:
	display(store)
	# display(store['key'].head())

# df['val'] and store['key'] is not properties in the dictionaries.
# This objects are just implementing getitem protocol.
