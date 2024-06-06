import numpy as np

data = np.array([[1, 2], [3, 4], [5, 6]]) #initialization

print(type(data)) # returns the object's type

print(data.ndim) # returns the dimensionality of the object, 1 for flat, 2 for nested, and so on

print(data.size) # returns the totat count of elements in the array

print(data.shape) # returns a tuple representing the x and y axes

print(data.dtype) # returns the data type of the elements

print(data.nbytes) # returns the number of bytes

print(data) # prints the array

# creating arrays with specified types

print(np.array([1., 2., 3.], dtype=np.int32)) # initialized with float values "dtype=np.int32" makes them integers

print(np.array([1, 2, 3], dtype=np.float32)) # initialized with int values "dtype=np.float32" makes them floats

print(np.array([1, 2, 3], dtype=np.complex128)) # initialized with either int or float "dtype=np.complex128" makes them complex

int_array = np.array([1,2,3],dtype=np.int32) # create an array of type int

print(int_array, int_array.dtype)

float_array = np.array(int_array,dtype=np.float32) # use the same array and typecast into the type of float

print(float_array, float_array.dtype)

astype_int = np.array(float_array.astype(np.int32)) # using astype function and initialize

print(astype_int)

print(astype_int.astype(np.complex128)) # or typecast to complex

#computing with numpy arrays and type promotion

x = np.array([1,2,3],dtype=np.float32)

y = np.array([1,2,3],dtype=np.int32)

print(x + y, (x + y).dtype) # results in an array of type float

z = np.array([-1,2,3])

# print(np.sqrt(z)) -> error! can't square a negative number

#to fix, convert the array to the type complex

print(np.sqrt(z.astype(np.complex128)))

print(np.sqrt(np.array([-1,2,3],dtype=np.complex128)))

# real and imaginary parts of elements in an array

arr = np.array([1,2,3],dtype=np.complex128)

print(arr)

print(arr.real, np.real(arr)) # gets the real part

print(arr.imag, np.imag(arr)) # gets the imaginary part
