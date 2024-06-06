import numpy as np

# creating uninitialized arrays and arrays with properties of other arrays

e = np.empty(10,dtype=np.int32) # np.empty generates a 1d array with 10 random arbitrary elements in it
"""
for i in range(e.shape[0]):
	e[i] = some value # np.empty arrays can be filled with values manually using loops and comprehensions

e.fill(10) # or using the fill with a constant value

np.empty can also have a tuple of x and y values to create multi-dimensional arrays
"""

print(e)

def f(x):
    """ function f takes an numpy array as parameter 
    the following are some of the ways we can use x to build arrays from 
    np.ones creates an array filled with 1s using the shape of x
    np.zeros does the same thing
    np.full_like requires a value (5.5) to be used as filler
    np.empty_like creates an array with the shape of x, but the elements are arbitrary"""
  
	return np.ones_like(x), np.zeros_like(x), np.full_like(x,5.5,dtype=np.float32), np.empty_like(x,dtype=np.float32)

a = np.array([1,2,3])
print(a)
print(f(a))
