import numpy as np

# indexing and slicing schemes for 1d arrays

a = np.arange(0, 11) # [0,1,2,3,4,5,6,7,8,9,10]
print(a[0]) # gets the element at 0th index (0)
print(a[-1],a[a.shape[0]-1]) # gets the last element
print(a[1:-1]) # starts from index 1 up to n-1 (not including the last element in the array)
print(a[1:-1:2]) # get every 2nd element from index 1 to n-1 
print(a[:5]) # select the first five elements
print(a[-5:]) # select the last five elements
print(a[::-1]) # reverse the order of the array
print(a[::-2]) # reverse the order of the array but only get every 2nd element

# indexing and slicing schemes for multi-dimensional arrays

def func(m,n):
	return n + 10 * m

B = np.fromfunction(func,(6,6),dtype=np.int32) # the lambda function "lambda m,n: n + 10 * m" can also be used
print(B)

# all rows, numerous ways to extract elements from columns
print(B[:,:]) # says get me all the rows and columns
print(B[:,2]) # says get me all the rows, but only get the 0th element from all the columns
print(B[:,:2]) # says get me all the rows, but only get the the first two elements from all the columns
print(B[:,-2:]) # says get me all the rows, but only get the the last two elements from all the columns
print(B[:,1:-1]) # says get me all the rows, but only get the elements from index 1 to n-1 from all the columns
print(B[:,::-1]) # says get me all the rows, but reverse the order of elements from all the columns
print(B[:,::2]) # says get me all the rows, but only get every 2nd element from all the columns

# numerous ways to extract elements from rows, all columns

print(B[1,:]) # says get me row 1, and all it's column's elements
print(B[-1,:]) # says get me the last row, and all it's column's elements
print(B[:2,:]) # says get me the first 2 rows, and all it's column's elements
print(B[-2:,:]) # says get me the last 2 rows, and all it's column's elements
print(B[1:-1,:]) # says get me the rows from index 1 to n-1, and all it's column's elements
print(B[::-1,:]) # reverses the order of the rows, and all it's column's elements remain in order
print(B[::2,:]) # says get me every 2nd row, and all it's column's elements

#combing some indexing and slicing schemes for both rows and columns

print(B[1:-1,::2]) # gets rows from index 1 to n - 1, and gets the columns' every 2nd element
